from random import randint, sample


def swap_mutation(arr):
    """
    Swap Mutation
    In swap mutation, we select two positions on the chromosome at random,
    and interchange the values. This is common in permutation based encodings.
    """
    if arr is None or len(arr) < 2:
        return ValueError()

    n = len(arr)
    first_pos = randint(0, n//2)
    second_pos = randint(n//2, n-1)

    arr[first_pos], arr[second_pos] = arr[second_pos], arr[first_pos]


def scramble_mutation(arr):
    """
    Scramble Mutation
    Scramble mutation is also popular with permutation representations.
    In this, from the entire chromosome, a subset of genes is chosen and their values are scrambled or shuffled randomly.
    """
    if arr is None or len(arr) < 2:
        return ValueError()
    
    n = len(arr)
    start_point = randint(0, n//2)
    end_point = randint(n//2, n-1)

    shuffled_subset = sample(arr[start_point:end_point], end_point-start_point)

    for i in range(start_point, end_point):
        arr[i] = shuffled_subset[i-start_point]

def inversion_mutation(arr):
    """
    Inversion Mutation
    In inversion mutation, we select a subset of genes like in scramble mutation,
    but instead of shuffling the subset, we merely invert the entire string in the subset.
    """
    if arr is None or len(arr) < 2:
        return ValueError()
    
    n = len(arr)
    start_point = randint(0, n//2)
    end_point = randint(n//2, n-1)

    subset = arr[start_point:end_point]

    for i in range(start_point, end_point):
        arr[i] = subset[end_point-i]
    
