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
        times.append(job_times)

    return times


def execute_factory_cycle(task_times):
    m0 = create_machine(0, 1)
    m1 = create_machine(1, 2)
    m2 = create_machine(2, 2)
    machines = [m0, m1, m2]
    jobs = [create_job(i, t) for i, t in enumerate(task_times)]
    f = Factory(machines, jobs)
    f.start()
    return f.statistics


def iterate(population, iteration=6, curr_iteration=0):
    if curr_iteration >= iteration:
        return

    population = create_population(task_times, 6)
    population_results = []
    for i, pop in enumerate(population):
        stats = execute_factory_cycle(pop)
        print("\n--  ITERATION %d / POPULATION %d --\n" % (curr_iteration+1, i+1))
        stats.pretty_print()
        population_results.append([i, stats.last_execution_time])

    population_results.sort(key=lambda x: x[1])
    best_three_children = [population[pop[0]] for pop in population_results[:3]]
    mutated_population = []
    for i in range(len(best_three_children)):
        p1 = best_three_children[i]
        for j in range(i+1, len(best_three_children)):
            p2 = best_three_children[j]
            c1, c2 = order_crossover(p1, p2)
            swap_mutation(c1)
            swap_mutation(c2)
            mutated_population += [c1, c2]

    iterate(mutated_population, curr_iteration= curr_iteration+1)


task_times = get_task_times()
population = create_population(task_times, len(task_times))
iterate(population)
