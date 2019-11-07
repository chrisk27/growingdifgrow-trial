"""
Contains function for each "elementary process" defined in the original Differential Growth Paper.
One of these functions will be called for each event that occurs.
For the original Differential Growth Paper, see the Resources folder.
"""


def birthX(well):
    """If the chosen well is empty, will create an xantophore"""
    if well == 'S':
        return 'X'
    else:
        return well


def birthM(well):
    """If the chosen well is empty, will create a melanophore"""
    if well == 'S':
        return 'M'
    else:
        return well


def short_kill(well, neighbor):
    """If the well and it's randomly selected neighbor are opposite chromaphores, kill the well"""
    if ((well == 'X') & (neighbor == 'M')) | ((well == 'M') & (neighbor == 'X')):
        return 'S'
    else:
        return well


def long_birth(well, origin):
    """If the well is empty and the well h distance away is an xantophore, create a melanophore"""
    if (well == 'S') & (origin == 'X'):
        return 'M'
    else:
        return well
