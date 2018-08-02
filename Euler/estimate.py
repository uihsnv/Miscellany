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
Estimate 'e', and plot the frequency distribution of contributing sum lenghts
'''

from math import floor, e as e_def
from matplotlib import pyplot as plt
from euler import gnedenko

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
