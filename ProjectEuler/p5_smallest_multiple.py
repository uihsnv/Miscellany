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
Smallest multiple

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from time import process_time

START = process_time()

# Natural number upto which to check for divisibility
N = 20

# A list of primes encountered
PRIME_LIST = []
# A list representing the full factorisation of the Least Common Multiple
# Each entry corresponds to the frequency of primes in the PRIME_LIST
LCM_FACTOR_FREQ = []

for natural in range(2,N+1):
    # Generate a list containing the frequencies of prime factors of each number
    FACTOR_FREQ = [0 for _ in PRIME_LIST]
    for i, p in enumerate(PRIME_LIST):
        # cycle through all the primes
        while natural % p == 0:
            natural = natural // p
            FACTOR_FREQ[i] += 1
        # if existing primes exhaust the number, then we have it's factorisation
        if natural == 1:
            # compare with the frequency list of the LCM
            # if a number has an excess of any prime, use that freq for the LCM
            for n, x in enumerate(FACTOR_FREQ):
                if x > LCM_FACTOR_FREQ[n]:
                    LCM_FACTOR_FREQ[n] = x
            break
    # otherwise, what remains is a prime
    else:
        PRIME_LIST.append(natural)
        LCM_FACTOR_FREQ.append(1)


# Reconstruct the LCM from the prime factors and their frequencies
LCM = 1
for idx, prime in enumerate(PRIME_LIST):
    LCM *= prime**LCM_FACTOR_FREQ[idx]


FINISH = process_time()
#print(PRIME_LIST)
#print(LCM_FACTOR_FREQ)
print(LCM)
print(f"{FINISH-START:.5f} seconds")
