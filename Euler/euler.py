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
Module to estimate 'e' (Euler's number), and further generalisations.
'''

from os import urandom
from math import floor
from random import seed, random

def gnedenko(number_of_samples, sum_limit, freq_length=0):
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
    # Quantity used due to a finite sampling of the frequency distribution
    floor_sum_limit_plus_1 = floor(sum_limit) + 1
    # Boolean tracking a non-zero freq_length
    non_zero_fl = (freq_length != 0)
    # Initialise list to contain the counts of each sum
    if non_zero_fl:
        frequencies = [0 for _ in range(freq_length)]

    for _ in range(number_of_samples):

        temp_sum = 0.0
        count = 0

        while temp_sum < sum_limit:
            temp_sum += random()
            count += 1

        e_estimate += count
        if non_zero_fl and (count < (floor_sum_limit_plus_1 + freq_length)):
            frequencies[count - floor_sum_limit_plus_1] += 1

    e_estimate /= number_of_samples
    frequencies = [(x/number_of_samples) for x in frequencies]

    if non_zero_fl:
        return e_estimate, frequencies

    return e_estimate

# Seeding the random number generator with 4 bytes of random data from the system
seed(urandom(4))
