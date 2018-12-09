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
"""
Largest prime factor

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

# The number, the largest factor of which, we must find
N = 600851475143

# The variable for the largest prime factor
# Initialised with the smallest prime
OPTIMUS_PRIME = 2

# Eliminating 2 as a factor, so that we only need to consider odd numbers after
while (N % OPTIMUS_PRIME == 0):
    N = N // OPTIMUS_PRIME

for i in range(3,int(sqrt(N)),2):
    OPTIMUS_PRIME = i
    while (N % OPTIMUS_PRIME == 0):
        N = N // OPTIMUS_PRIME
        if N == 1:
            print(OPTIMUS_PRIME)
            exit()

# If the program has reached this point, then N is a prime
print(N)
