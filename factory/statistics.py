from os import name
from factory import job


class MachineStatistics:

    def __init__(self, timer, machine_ids) -> None:
        self.timer = timer
        self.machine_records = {id: {} for id in machine_ids}
        self.last_execution_time = 0

    def record_job_done(self, machine_id, job_id, machine_name):
        current_time = self.timer.get_current_time()
        current_job_record = {"job_id": job_id,
                              "end_time": current_time}
        if machine_name not in self.machine_records[machine_id]:
            self.machine_records[machine_id][machine_name] = []
        self.machine_records[machine_id][machine_name].append(
            current_job_record)

        self.last_execution_time = max(self.last_execution_time, current_time)

    def notify(self, machine_id, job_id, machine_name):
        self.record_job_done(machine_id, job_id, machine_name)

    def __calculate_last_execution_time_for_each_partition(self, partition_records):
        last_execution_time = 0
        execution_times = {}
        for machine_name, records in partition_records.items():
            current_execution_time = max(
                [record['end_time'] for record in records])
            execution_times[machine_name] = current_execution_time
            last_execution_time = max(
                last_execution_time, current_execution_time)

        return execution_times, last_execution_time

    def pretty_print(self):
        for m_id, job_records in self.machine_records.items():
            execution_times, last_execution_time = self.__calculate_last_execution_time_for_each_partition(
                job_records)
            print("Machine ID: %s\nLastExecutionTime: %d\nEach Partition Execution Times: %s\n-----------------------------" %
                  (m_id, last_execution_time, execution_times))
