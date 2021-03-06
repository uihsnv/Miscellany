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
Even Fibonacci numbers

    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
"""

from time import process_time

START = process_time()

# The number below which the the Fibonacci sequence must terminate
NUMBER_LIMIT = 4000000

# Values storing the current and previous values of the sequence
FIBONACCI = 1
FIB_OLD = 1

# Boolean values to account for even elements
TOGGLE = False
TGL_OLD = False

SUM = 0

while FIBONACCI < NUMBER_LIMIT:

    FIB_OLD, FIBONACCI = FIBONACCI, FIB_OLD + FIBONACCI

    # Even numbers occur at every 3rd element
    # and the toggle is True at every 3rd element
    TGL_OLD, TOGGLE = TOGGLE, (TOGGLE == TGL_OLD)

    if TOGGLE:
        SUM += FIBONACCI

FINISH = process_time()
print(SUM)
print(f"{FINISH-START:.5f} seconds")
