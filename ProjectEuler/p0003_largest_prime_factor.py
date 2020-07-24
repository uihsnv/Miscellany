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

from sys import exit as sexit
from math import sqrt
from time import process_time

START = process_time()

# The number, the largest factor of which, we must find
N = 600851475143
SQRT_N = int(sqrt(N))

def fin(optimus_prime=1):
    """
    Ending the program when the largest prime factor is found
    """
    finish = process_time()
    print(optimus_prime)
    print(f"{finish-START:.5f} seconds")
    sexit()

# Eliminating 2 as a factor, so that we only need to consider odd numbers after
while N % 2 == 0:
    N = N // 2
if N == 1:
    fin(2)

# Scan upto sqrt(N), because there can atmost be one prime factor greater than that
for i in range(3, SQRT_N, 2):
    while N % i == 0:
        N = N // i
    if N == 1:
        fin(i)

# If the program has reached this point, then N is a prime,
# or the largest prime factor is greater than the square root of N
fin(N)
