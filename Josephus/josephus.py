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
A program simulating outcomes of the Josephus problem.

    Where does one sit in a circle, if one is to survive a ritual
    where, in some order, and with some starting position, each person
    killed the person sitting next to them.

Motivated by the video: "The Josephus Problem - Numberphile":
    https://www.youtube.com/watch?v=uCsD3ZGzMgE
"""

TOTAL = 6
PEOPLE = [i+1 for i in range(TOTAL)]

NUM_PEOPLE = len(PEOPLE)

while NUM_PEOPLE > 1:

    PEOPLE = PEOPLE[::2]

    if NUM_PEOPLE % 2 != 0:
        PEOPLE = PEOPLE[-1:] + PEOPLE[:-1]

    NUM_PEOPLE = len(PEOPLE)

print(PEOPLE[0])
