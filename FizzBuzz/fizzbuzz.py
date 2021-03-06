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
A program simulating a game of FizzBuzz
    Give a continuous, ordered stream of the integers, say:
    Fizz when a multiple of 3
    Buzz when a multiple of 5
    FizzBuzz when a multiple of both

Motivated by the video: "FizzBuzz: One Simple Interview Question"
Episode 2, Season 1 of the series: "The Basics"
    https://www.youtube.com/watch?v=QPZ0pIK_wsc
"""

TOTAL = 35
FIZZ = 3
BUZZ = 5
NULL = ''

for i in range(TOTAL):
    MESSAGE = NULL
    if i % FIZZ == 0:
        MESSAGE += 'Fizz'
    if i % BUZZ == 0:
        MESSAGE += 'Buzz'
    if MESSAGE == NULL:
        MESSAGE = f'{i}'
    print(MESSAGE)
