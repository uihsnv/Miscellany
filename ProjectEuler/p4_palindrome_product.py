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

START = process_time()

# The number of digits the numbers, whose product is the
# largest palindrome, need to be
N = 2

# The square of the largest N-digit number

LARGE_N_SQ = 0

for i in range(N):
    LARGE_N_SQ += 9*(10**i)

LARGE_N_SQ *= LARGE_N_SQ

# Now find the nearest palindrome less than or equal to it,
# and check to see if it has an N-digit factor couplet.
# Otherwise rinse and repeat


FINISH = process_time()
print(SUM)
print(f"{FINISH-START:.5f} seconds")
