#!/usr/bin/env python3
#
#   Copyright (C) 2018  Vishnu V. Krishnan : vishnugb@gmail.com
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
'''
Estimating 'e' (Euler's number), and further generalisations.
'''

from os import urandom
from math import floor, e as e_def
from random import seed, random
from matplotlib import pyplot as plt

def gnedenko(number_of_samples, extreme, freq_length):
    '''
    An estimate of `e' as the expectation of
    a random variable that is the number of uniform
    r.v.s such that their sum just exceeds 1

    Reference:
    Estimating the Value of e by Simulation
    K. G. Russell
    The American Statistician
    https://www.jstor.org/stable/2685243
    '''

    # Initialise estimate value to 0
    e_estimate = 0.0
    # Initialise list to contain the counts of each sum
    frequencies = [0 for _ in range(freq_length)]
    # Quantity used due to a finite sampling of the frequency distribution
    floor_extreme_plus_1 = floor(extreme) + 1

    for _ in range(number_of_samples):

        temp_sum = 0.0
        count = 0

        while temp_sum < extreme:
            temp_sum += random()
            count += 1

        e_estimate += count
        if count < (floor_extreme_plus_1 + freq_length):
            frequencies[count - floor_extreme_plus_1] += 1

    e_estimate /= number_of_samples
    frequencies = [(x/number_of_samples) for x in frequencies]

    return e_estimate, frequencies

# Seeding the random number generator with 4 bytes of random data from the system
seed(urandom(4))

# The number of sum-samples, which you'd like to see frequences for
HIST_LENGTH = 7
# When SUM is set to '1', the estimate is for `e'
SUM = 1
# The total number of Uniform random numbers to use
N = 100000

DATA = gnedenko(N, SUM, HIST_LENGTH)
plt.bar([j+1+floor(SUM) for j in range(HIST_LENGTH)], DATA[1])
plt.title("Frequency distribution of the number of Uniform samples required, \n"
          "for their sum to exceed unity")
plt.annotate(f"Defined e : {e_def}", xy=(0.5, 0.9), xycoords='axes fraction')
plt.annotate(f"Estimate  : {DATA[0]}", xy=(0.5, 0.85), xycoords='axes fraction')
plt.annotate(f"No. of samples = {N:,}", xy=(0.5, 0.8), xycoords='axes fraction')
plt.show()
