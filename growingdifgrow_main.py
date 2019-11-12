"""
This script runs the basic simulations for Differential Growth Turing Pattern Formation.
It is the same process that is described in the original Differential Growth Paper.

To change parameters, such as rate constants and lattice size, edit text below prior to running.

Also, will need to set a time limit (Number of cycles through the lattice) until I can program a manual stop.
"""

from datetime import datetime
import random
import matplotlib.pyplot as plt

from growingdifgrow.processes import baseprocess, neighborcalc
from growingdifgrow import initialconditions


def sim_parameters():
    """This function defines the initial parameters used in the experiments"""
    global rows, cols, h, iterations
    rows = 100  # splitting lattice dimensions to rows and columns in case we don't want a square
    cols = 100
    h = 15  # characteristic distance, should be half of the wavelength
    iterations = 1000


def reaction_rates():
    """This function defines the reaction rates for each process"""
    global bx, bm, dx, dm, sm, sx, lx
    bx = 1  # birth of xantophores
    bm = 0  # birth of melanophores

    dx = 0  # natural death of xantophores
    dm = 0  # natural death of melanophores

    sm = 1  # short-range killing of xantophore by melanophore
    sx = 1  # short-range killing of melanophore by xantophore
    lx = 2.5  # long-range activation/birth strength


def sim_setup():
    """This function sets up the simulation, calling initial conditions and probabilities"""
    array, irid_array = initialconditions.blank(rows, cols)
    sum_rates = bx + bm + dx + dm + sm + sx + lx
    event_list = ['birthX', 'birthM', 'deathX', 'deathM', 'killX', 'killM', 'activateM']
    probability_list = [bx / sum_rates, bm / sum_rates, dx / sum_rates, dm / sum_rates,
                        sm / sum_rates, sx / sum_rates, lx / sum_rates]
    return array, irid_array, event_list, probability_list


def run_sim(array, irid_array, event_list, probability_list):
    """This function runs the simulations and outputs the final matrix"""
    num_events = rows * cols
    for loop in range(iterations):
        idx0 = random.choices(range(rows), k=num_events)
        idx1 = random.choices(range(cols), k=num_events)
        events = random.choices(event_list, weights=probability_list, k=num_events)

        for i in range(num_events):
            location = (idx0[i], idx1[i])
            well = array[location]
            if events[i] == 'activateM':
                point = neighborcalc.hdist_angle(location, array, h=h)
                array[location] = baseprocess.long_birth(well, point, irid_array[location])
            elif events[i] == 'killX':
                neigh = neighborcalc.nearest_neighbor(location, array, size=4)
                array[location] = baseprocess.short_kill_x(well, neigh)
            elif events[i] == 'killM':
                neigh = neighborcalc.nearest_neighbor(location, array, size=4)
                array[location] = baseprocess.short_kill_m(well, neigh)
            elif events[i] == 'birthX':
                array[location] = baseprocess.birth_x(well)
            elif events[i] == 'birthM':
                array[location] = baseprocess.birth_m(well, irid_array[location])
            elif events[i] == 'deathX':
                array[location] = baseprocess.death_x(well)
            elif events[i] == 'deathM':
                array[location] = baseprocess.death_m(well)

    return array


def plotter(array):
    """This function can plot the arrays in a manner similar to the original paper:
    Yellow pixels are xantophores
    Black pixels are melanophores
    White pixels are empty ('S')
    """


if __name__ == '__main__':
    startTime = datetime.now()
    sim_parameters()
    reaction_rates()
    system, irid, event, prob_list = sim_setup()
    final = run_sim(system, irid, event, prob_list)
    print(datetime.now() - startTime)
