import logging

from factory import Factory, create_machine, create_job
from genetic_algorithm import create_population, order_crossover, swap_mutation

logging.basicConfig(level=logging.INFO)

def get_task_times():
    times = []

    lines = []
    with open('data/data5.txt', 'r', encoding='utf-8') as file:
        lines = file.read().split("\n")

    # First line skipped because unnecessary information
    for i in range(1, len(lines)):
        job_times = list(map(int, lines[i].split()))
        times.append([job_times[0], job_times[1]])
    
    return times

def iterate(task_times, iteration=6, curr_iteration= 0):
    if curr_iteration >= iteration:
        return

    population = create_population(task_times, 6)
    for pop in population:
        print(pop)
        m0 = create_machine(0, 1)
        m1 = create_machine(1, 2)
        machines = [m0, m1]
        jobs = [create_job(i, t) for i, t in enumerate(task_times)]
        f = Factory(machines, jobs)
        f.start()

        # After the result apply crossover and mutation

task_times = get_task_times()
iterate(task_times)