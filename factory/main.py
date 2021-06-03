import logging


import logging

from factory import Factory
from machine import create_machine
from job import create_job

logging.basicConfig(level= logging.INFO)

m0 = create_machine(0, 2)
m1 = create_machine(1, 2)

j0 = create_job(0, [5, 2])
j1 = create_job(1, [3, 1])
j2 = create_job(2, [1, 4])
j3 = create_job(3, [2, 7])

f = Factory([m0, m1], [j0, j1, j2, j3])
f.start()
