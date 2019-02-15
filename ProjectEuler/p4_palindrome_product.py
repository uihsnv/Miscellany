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
Largest palindrome product

    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

from time import process_time
from math import log10

START = process_time()

# The number of digits the numbers, whose product is the
# largest palindrome, need to be
N = 2


def is_palindrome(sample):
    """
    Function to check if a number is a palindrome
    """
    digits = int(log10(sample)) + 1
    maleable = str(sample)
    for i in range(digits // 2):
        if  maleable[i] != maleable[digits-i-1]:
            return False
    else:
        return True

def has_2_N_digit_factors(sample):
    """
    A check for if the number has two N-digit factors
    """


LARGE_N_SQ = 0
# The largest 'N' digit number
for i in range(N):
    LARGE_N_SQ += 9*(10**i)
# The square of the largest N-digit number
LARGE_N_SQ *= LARGE_N_SQ

# The square of the smallest N-digit number
SMALL_N_SQ = (10**(N-1))**2

print(LARGE_N_SQ, SMALL_N_SQ)

# Now find the nearest palindrome less than or equal to it,
# and check to see if it has an N-digit factor couplet.
# Otherwise rinse and repeat
for j in range(LARGE_N_SQ, SMALL_N_SQ, -1):
    if is_palindrome(j): #and has_2_N_digit_factors(j):
        print(j)
        break
else:
    print(f"There are no palindromic integers with {N}-digit factors")

FINISH = process_time()
print(f"{FINISH-START:.5f} seconds")
