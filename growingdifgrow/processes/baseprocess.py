"""
Contains function for each "elementary process" defined in the original Differential Growth Paper.
One of these functions will be called for each event that occurs.
For the original Differential Growth Paper, see the Resources folder.
"""


def birth_x(well):
    """If the chosen well is empty, will create an xantophore"""
    if well == 'S':
        return 'X'
    else:
        return well


def birth_m(well, irid):
    """If the chosen well is empty and isn't the location of an iridophore, will create a melanophore"""
    if (well == 'S') & (~ irid):
        return 'M'
    else:
        return well


def death_x(well):
    """If the well is a xantophore, kill it"""
    if well == 'X':
        return 'S'
    else:
        return well


def death_m(well):
    """If the well is a melanophore, kill it"""
    if well == 'M':
        return 'S'
    else:
        return well


def short_kill_m(well, neighbor):
    """If the well is xantophore and neighbor is melanophore, kill the xantophore"""
    # Note that original paper assumes that the chromaphores kill each other at the same rate (sm == sx == s)
    if (well == 'X') & (neighbor == 'M'):
        return 'S'
    else:
        return well


def short_kill_x(well, neighbor):
    """If the well is melanophore and neighbor is xantophore, kill the melanophore"""
    # Note that original paper assumes that the chromaphores kill each other at the same rate (sm == sx == s)
    if (well == 'M') & (neighbor == 'X'):
        return 'S'
    else:
        return well


def long_birth(well, origin, irid):
    """If the well is empty and the well h distance away is an xantophore, create a melanophore"""
    if (well == 'S') & (origin == 'X') & (~ irid):
        return 'M'
    else:
        return well
