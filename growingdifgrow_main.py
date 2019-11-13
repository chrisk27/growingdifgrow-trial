"""
This script runs the basic simulations for Differential Growth Turing Pattern Formation.
It is the same process that is described in the original Differential Growth Paper.

To change parameters, such as rate constants and lattice size, edit text below prior to running.

Also, will need to set a time limit (Number of cycles through the lattice) until I can program a manual stop.
"""

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

from growingdifgrow.processes import neighborcalc
from growingdifgrow import initialconditions


def sim_parameters():
    """This function defines the initial parameters used in the experiments"""
    global rows, cols, h, process_per_cycle, num_cycle
    rows = 100  # splitting lattice dimensions to rows and columns in case we don't want a square
    cols = 100
    h = 15  # characteristic distance, should be half of the wavelength
    process_per_cycle = 10**7
    num_cycle = 10**2


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
    event_list = np.array(['birthX', 'birthM', 'deathX', 'deathM', 'killX', 'killM', 'activateM'])
    probability_list = np.array([bx / sum_rates, bm / sum_rates, dx / sum_rates, dm / sum_rates,
                                 sm / sum_rates, sx / sum_rates, lx / sum_rates])
    return array, irid_array, event_list, probability_list


def run_sim(array, irid_array, event_list, probability_list, num_loop=100, per_loop=10**7):
    """This function runs the simulations and outputs the final matrix"""
    if (rows > 255) | (cols > 255):
        idx_type = np.uint16
    else:
        idx_type = np.uint8
    for loop in range(num_loop):
        idx0 = np.random.randint(low=0, high=rows, size=per_loop, dtype=idx_type)
        idx1 = np.random.randint(low=0, high=cols, size=per_loop, dtype=idx_type)
        events = np.random.choice(event_list, size=per_loop, replace=True, p=probability_list)

        for i in range(per_loop):
            location = (idx0[i], idx1[i])
            well = array[location]

            if events[i] == 'activateM':
                if (well == 'S') & (~ irid_array[location]):
                    point = neighborcalc.hdist_angle(location, array, h=h)
                    if point == 'X':
                        array[location] = 'M'
                    else:
                        continue
                else:
                    continue

            elif events[i] == 'killX':
                if well == 'M':
                    neigh = neighborcalc.nearest_neighbor(location, array, size=4)
                    if neigh == 'X':
                        array[location] = 'S'
                    else:
                        continue
                else:
                    continue

            elif events[i] == 'killM':
                if well == 'X':
                    neigh = neighborcalc.nearest_neighbor(location, array, size=4)
                    if neigh == 'M':
                        array[location] = 'S'
                    else:
                        continue
                else:
                    continue

            elif events[i] == 'birthX':
                if well == 'S':
                    array[location] = 'X'
                else:
                    continue

            elif events[i] == 'birthM':
                if well == 'S':
                    array[location] = 'M'
                else:
                    continue

            elif events[i] == 'deathX':
                if well == 'X':
                    array[location] = 'S'
                else:
                    continue

            elif events[i] == 'deathM':
                if well == 'M':
                    array[location] = 'S'
                else:
                    continue

    return array


def plotter(array):
    """This function can plot the arrays in a manner similar to the original paper:
    Yellow pixels are xantophores
    Black pixels are melanophores
    White pixels are empty ('S')
    """
    img = np.empty((array.shape[0], array.shape[1], 3), dtype=np.float32)
    img[array == 'S', :] = [1, 1, 1]  # sets empty spots on array to white
    img[array == 'M', :] = [0, 0, 0]  # sets melanophores to black
    img[array == 'X', :] = [1, 1, 0]  # sets xantophores to yellow
    return img


if __name__ == '__main__':
    startTime = datetime.now()
    sim_parameters()
    reaction_rates()
    system, irid, event, prob_list = sim_setup()
    final = run_sim(system, irid, event, prob_list)#, num_loop=num_cycle, per_loop=process_per_cycle)
    imag = plotter(final)
    print(datetime.now() - startTime)
    plt.imshow(imag)
    plt.show()

