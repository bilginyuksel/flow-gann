from random import sample


def create_population(arr, population_count):
    """
    creates a population from given arr.
    it will shuffle the original arr multiple times and creates a population
    based on shuffled arrays.
    """
    return [sample(arr, len(arr)) for _ in range(population_count)]
