"""
This module  determines which neighbor is chosen for comparison to the given well.
These values will be passed into the other process functions.
Common inputs:
    loc (type = 1x2 array): the location on the array of the well in question
    array (type = np.array): the array that corresponds to the state of the system
    h (type  = int > 0): the interaction distance
    size (type = int): the number of nearest neighbors to consider. Should be 4 or 8, will automatically default to 4.
"""

import math
import random


def nearest_neighbor(loc, array, size=4):
    """Chooses a random nearest neighbor"""
    row = array.shape[0]
    col = array.shape[1]
    r = loc[0]
    c = loc[1]
    left1 = (r - 1) % row
    right1 = (r - 1) % row
    down1 = (c - 1) % col
    up1 = (c - 1) % col
    if size != 4 | size != 8:
        size = 4  # default value. May add 12 functionality later
    if size == 4:
        neighborlist = [(left1, c), (right1, c), (r, down1), (r, up1)]
    else:
        neighborlist = [(left1, c), (right1, c), (r, down1), (r, up1),
                        (left1, down1), (left1, up1), (right1, down1), (right1, up1)]
    return array[random.choice(neighborlist)]


def hdist_angle(loc, array, h=15):
    """Chooses a random point h away for long range process"""
    angle = random.random() * 2 * math.pi
    neighx = round(loc[0] + h * math.cos(angle)) % array.shape[0]
    neighy = round(loc[1] + h * math.sin(angle)) % array.shape[1]
    return array[neighx, neighy]
