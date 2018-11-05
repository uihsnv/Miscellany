!
!   Copyright (C) 2018  Vishnu V. Krishnan : vishnugb@gmail.com
!
!   This program is free software: you can redistribute it and/or modify
!   it under the terms of the GNU General Public License as published by
!   the Free Software Foundation, either version 3 of the License, or
!   (at your option) any later version.
!
!   This program is distributed in the hope that it will be useful,
!   but WITHOUT ANY WARRANTY; without even the implied warranty of
!   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!   GNU General Public License for more details.
!
!   You should have received a copy of the GNU General Public License
!   along with this program.  If not, see <https://www.gnu.org/licenses/>.
!
PROGRAM ackermann

    IMPLICIT NONE

    REAL :: start, finish
    INTEGER, PARAMETER :: a=4
    INTEGER, PARAMETER :: b=2

    IF ( (a .LT. 0) .OR. (b .LT. 0) ) ERROR STOP "One of the integers is negative"

    CALL CPU_TIME(start)

    PRINT*, ackermann_peter(a, b)

    CALL CPU_TIME(finish)
    PRINT*, "CPU time = ", finish - start

    CONTAINS

        INTEGER PURE RECURSIVE FUNCTION ackermann_peter(m, n) RESULT(ack)

            INTEGER, INTENT(IN) :: m, n

            IF (m .EQ. 0) THEN
                ack = n + 1
            ELSE IF (n .EQ. 0) THEN
                ack = ackermann_peter(m-1, 1)
            ELSE
                ack = ackermann_peter(m-1, ackermann_peter(m, n-1))
            END IF

        END FUNCTION

END PROGRAM ackermann
