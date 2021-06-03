import logging
from typing import List


class Job:
    """
    Job will have process time for each machine
    """

    def __init__(self, id, process_times) -> None:
        self.id = id
        self.curr_handler = 0
        self.process_times = process_times

    def is_done(self, machine_id):
        return self.process_times[machine_id] <= 0

    def is_completely_done(self):
        for time in self.process_times:
            if time > 0:
                return False
        return True

    def execute(self, machine_id):
        if self.is_done(machine_id):
            logging.warning("Trying to process already finished job")
            return

        self.process_times[machine_id] -= 1

    def current_handler(self):
        return self.curr_handler

    def next_handler(self):
        self.curr_handler += 1
        return None if self.curr_handler >= len(self.process_times) else self.curr_handler

    def notify(self):
        """
        Machine will notify when the job is done.
        So call the next machine when this function triggered
        """
        self.curr_handler.job_done.add(self.id)
        self.next()


def create_job(id, process_times: List[int]) -> Job:
    return Job(id, process_times)
