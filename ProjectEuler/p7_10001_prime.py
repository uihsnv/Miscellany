#!/usr/bin/env python3
#
#   Copyright (C) 2019  Vishnu V. Krishnan : vishnugb@gmail.com
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
10001st prime

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10001st prime number?
"""

from time import process_time
from math import sqrt

START = process_time()

N = 10001
# Initialise the list with the second prime
PRIME_LIST = [3]

# Start with the third prime as a candidate
CANDIDATE = 5
# A count of primes accumulated in the PRIME_LIST
while len(PRIME_LIST) < N-1:
    # cycle through all the primes found
    SQRT_CANDIDATE = int(sqrt(CANDIDATE))
    for p in PRIME_LIST:
        if p > SQRT_CANDIDATE:
            PRIME_LIST.append(CANDIDATE)
            break
        elif CANDIDATE % p == 0:
            break
    # Increment by 2, since only odd numbers can be prime
    # This is also the reason we don't need '2' in the PRIME_LIST
    CANDIDATE += 2

FINISH = process_time()
print(PRIME_LIST[N-2])
print(f"{FINISH-START:.5f} seconds")
