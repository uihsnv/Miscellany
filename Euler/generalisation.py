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
Plot the estimate as a function of varying SUM values, there by obtaining a
generalised Euler 'number'
'''

from math import e as e_def
from matplotlib import pyplot as plt
from euler import gnedenko

# The number of data points you need in the plot
NUM_POINTS = 50
# A list of numbers representing the +ve real number line
SUMS = [x/10 for x in range(1, NUM_POINTS+1)]
# The total number of Uniform random numbers to use
N = 100000
# Find the generalised estimates
ESTIMATES = [gnedenko(N, SUMS[i])[0] for i in range(NUM_POINTS)]

plt.plot(SUMS, ESTIMATES, '.')
plt.plot((0, 5), (e_def, e_def))

plt.title("Estimates obtained from a generalisation of the Gnedenko \n"
          "defenition of Euler's number")
plt.annotate(f"No. of samples = {N:,}", xy=(0.1, 0.8), xycoords='axes fraction')
plt.show()
