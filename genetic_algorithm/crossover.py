from random import randint


def order_crossover(p1, p2):
    """
    OX1 is used for permutation based crossovers with the intention of transmitting information about relative ordering to the off-springs. It works as follows

        − Create two random crossover points in the parent and copy the segment between them from the first parent to the first offspring.
        - Now, starting from the second crossover point in the second parent, copy the remaining unused numbers from the second parent to the first child, wrapping around the list.
        - Repeat for the second child with the parent’s role reversed.
    """

    if p1 is None or p2 is None:
        raise ValueError(
            "order_crossover parent array parameters can't be null")

    if len(p1) != len(p2):
        return ValueError("order_crossover parent array lengths have be to equal")

    n = len(p1)
    temp_random_points = [randint(0, n), randint(0, n)]
    start_point = min(temp_random_points)
    end_point = max(temp_random_points)

    c1, c2 = [0 for _ in range(n)], [0 for _ in range(n)]
    # Put constant genes
    # Example result would be: [ , , 3, 5, 7, , ]
    for i in range(start_point, end_point):
        c1[i] = p1[i]
        c2[i] = p2[i]

    # remove cross duplicates
    for i in range(start_point, end_point):
        if p1[i] in c2:
            c2.remove(p1[i])
        if p2[i] in c1:
            c1.remove(p2[i])
    
    # add right elements of parent to left elements of child
    for i in range(end_point, n):
        c1[i-end_point] = p2[i]
        c2[i-end_point] = p1[i]

    # add left elements of parent to right elements of child
    for i in range(0, end_point):
        c1[end_point+i] = p2[i]
        c2[end_point+i] = p1[i]

    return c1, c2 