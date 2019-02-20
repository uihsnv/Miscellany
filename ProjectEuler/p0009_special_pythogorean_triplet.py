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
Special Pythagorean triplet

    A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which,

                    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

from time import process_time

START = process_time()

SUM = 1000

for i in range(1, SUM):
    for j in range(i+1, SUM-i):
        if i**2 + j**2 == (SUM-i-j)**2:
            FINISH = process_time()
            print(i, ' × ', j, ' × ', 1000-i-j, ' = ', i*j*(1000-i-j))
            print(f"{FINISH-START:.5f} seconds")
            break
    else:
        continue
    break
else:
    print("There is no number satisfying both conditions")
