import logging
from typing import List
from factory.statistics import MachineStatistics
from factory.machine import Machine
from factory.job import Job
from factory.global_time import Timer


class Factory:

    def __init__(self, machines: List[Machine], jobs: List[Job]) -> None:
        self.timer = Timer()
        self.statistics = MachineStatistics(
            self.timer, [m.id for m in machines])

        for machine in machines:
            machine.observers += [self, self.statistics]

        # check if jobs are matched with machines
        for job in jobs:
            if len(job.process_times) != len(machines):
                raise ValueError(
                    "job process time should be entered for every machine")

        self.machines = machines
        self.jobs = jobs

        self.__job_idx = -1

        self.job_done = [False for _ in range(len(jobs))]

    def start(self):
        starting_machine = self.machines[0]
        starting_machine.set_job(self.next_job())
        while self.__has_incomplete_jobs():
            self.timer.run_timer()
            if starting_machine.has_available_partition() and self.has_next_job():
                starting_machine.set_job(self.next_job())
            self.__execute_machines()
            # logging.info(self.job_done)
            # logging.info(self.statistics.machine_records)

        self.statistics.pretty_print()

    def notify(self, machine_id, job_id):
        # pass job to next handler
        finished_job = self.jobs[job_id]
        next_handler = finished_job.next_handler()
        if next_handler is None:  # job is offically done
            self.job_done[job_id] = True
            return

        # otherwise attach job to the next handler
        if next_handler >= len(self.machines):
            logging.error(
                "Index out of bounds error, next machine id is bigger than machines length")
            raise IndexError()

        self.machines[next_handler].set_job(finished_job)

    def has_next_job(self):
        return self.__job_idx + 1 < len(self.jobs)

    def next_job(self) -> Job:
        self.__job_idx += 1
        next_job = self.jobs[self.__job_idx]
        return next_job

    def __execute_machines(self):
        for machine in self.machines:
            machine.run()

    def __has_incomplete_jobs(self):
        return not all(self.job_done)
