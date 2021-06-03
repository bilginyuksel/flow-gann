class MachineStatistics:

    def __init__(self, timer, machine_names) -> None:
        self.timer = timer
        self.machine_records = {name: [] for name in machine_names}

    def __create_job_record(self, job_id):
        return {"job_id": job_id, "end_time": self.timer.get_current_time()}

    def record_job_done(self, machine_id, job_id):
        self.machine_records[machine_id].append(self.__create_job_record(job_id))

    def notify(self, machine_id, job_id):
        self.record_job_done(machine_id, job_id)

    def pretty_print(self):
        print("""
        ---  Factory execution end  ----

        Machine scores are printed below.
        ---------------------------------""")

        for m_id, job_records in self.machine_records.items():
            print("""       
        Machine ID: %s
        Records: %s
        
        -----------------------------""" % (m_id, job_records))