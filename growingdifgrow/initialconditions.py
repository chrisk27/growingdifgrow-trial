"""
This file can be used to generate some standard initial conditions.

Each initial state is stored as a function, whose arguments are the number of rows and columns.

The first output of each function is the initial array.
The second output is an array of 'iridophores', where if True then melanophores cannot form
"""

import numpy as np
from math import floor


def blank(rows, columns):
    """Generates an initial state with all empty cells (filled with 'S')"""
    output = np.empty([rows, columns], dtype=str)
    output.fill('S')
    return output, np.zeros((rows, columns), dtype=bool)


def iridophore_band(rows, columns, bandwidth=1):
    """Generates an initial empty state, except for an initial band of iridophores which pre-pattern the system"""
    output = np.empty([rows, columns], dtype=str)
    output.fill('S')
    irid = np.zeros([rows, columns], dtype=bool)
    irid[0:bandwidth, :] = True  # Assigns iridophores to a row
    irid = np.roll(irid, floor((rows - bandwidth) / 2), axis=0)  # rotates array so iridophores are in the middle
    return output, irid


def random_start(rows, columns, irid_ratio=0):
    """Generates a random starting condition, and a random distribution of iridophores at proportion = irid_ratio"""
    output = np.empty([rows, columns], dtype=str)
    output.fill('S')
    rand_array = np.random.rand(rows, columns)
    output[rand_array < 1/3] = 'X'
    output[rand_array > 2/3] = 'M'

    irid_rand = np.random.rand(rows, columns) < irid_ratio

    return output, irid_rand
