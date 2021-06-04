from collections import deque
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

    p1, p2 = p1.copy(), p2.copy()

    n = len(p1)
    
    start_idx = randint(0, n//2)
    end_idx = randint(n//2, n-1)

    p1_const_genes = p1[start_idx: end_idx]
    p2_const_genes = p2[start_idx: end_idx]

    c1, c2 = [], []

    # last part
    for i in range(end_idx, n):
        c1.append(p1[i])
        c2.append(p2[i])

    # first part
    for i in range(0, start_idx):
        c1.append(p1[i])
        c2.append(p2[i])

    # add const genes
    c1 += p1_const_genes
    c2 += p2_const_genes

    # remove duplicate
    for p1_gene, p2_gene in zip(p1_const_genes, p2_const_genes):
        if p1_gene in c1:
            c1.remove(p1_gene)
        if p2_gene in c2:
            c2.remove(p2_gene)

    child1 = deque(p1_const_genes.copy())
    child2 = deque(p2_const_genes.copy())

    for i in range(len(c1)):
        if i > start_idx:
            child2.appendleft(c1[i])
        else:
            child2.append(c1[i])
        
    for i in range(len(c2)):
        if i > start_idx:
            child1.appendleft(c2[i])
        else:
            child1.append(c2[i])

    return list(child1), list(child2)
