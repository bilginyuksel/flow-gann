
class Machine:
    """
    Machines can execute tasks and should be placed inside a factory.
    Machines can be linked together like a chain. When a new process
    started it should be executed by N machines. Machines could have multiple partitions.
    """

    def __init__(self, id, partition=1, observers=[]) -> None:
        self.id = id
        self.machine_id = "partition" + str(id)
        self.partition = partition
        self.job_queue = []
        self.observers = observers

        self.active_jobs = [None for _ in range(partition)]

    def has_available_partition(self):
        return any([job is None or job.is_done(self.id) for job in self.active_jobs])

    def set_job(self, job):
        """
        set a new job to current machine, if a machine still has unfinished jobs
        then add the new job to waiting queue
        """
        if self.has_available_partition():
            self.__set_job(job)  # set job to first available partition
        else:
            self.job_queue.append(job)

    def run(self):
        """
        run at each timespan spent inside a factory
        """
        for job in self.active_jobs:
            if job is None or job.is_done(self.id):
                continue

            job.execute(self.id)
            if job.is_done(self.id):
                self.notifyAll(self.id, job.id)

        if len(self.job_queue) > 0 and self.has_available_partition():
            self.__set_job(self.job_queue.pop(0))

    def notifyAll(self, machine_id, job_id):
        for observer in self.observers:
            observer.notify(self.id, job_id)

    def __set_job(self, job):
        for i in range(len(self.active_jobs)):
            if self.active_jobs[i] is None or self.active_jobs[i].is_done(self.id):
                self.active_jobs[i] = job
                return


def create_machine(id: int, partition: int = 1) -> Machine:
    return Machine(id, partition, observers=[])
