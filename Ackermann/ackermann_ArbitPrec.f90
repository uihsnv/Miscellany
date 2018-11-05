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

    USE FMZM

    IMPLICIT NONE

    REAL :: start, finish
    TYPE(IM) :: a, b, c

    CALL FM_SET(20)

    a = to_im(2)
    b = to_im(1)

    IF ( (a .LT. 0) .OR. (b .LT. 0) ) ERROR STOP "One of the integers is negative"

    CALL CPU_TIME(start)

    CALL IM_PRINT(ackermann_peter(a, b))

    CALL CPU_TIME(finish)
    PRINT*, "CPU time = ", finish - start

    CONTAINS

        TYPE(IM) RECURSIVE FUNCTION ackermann_peter(m, n) RESULT(ack)

            TYPE(IM), INTENT(IN) :: m, n
            CALL FM_ENTER_USER_FUNCTION(ack)

            IF (m .EQ. 0) THEN
                ack = n + 1
            ELSE IF (n .EQ. 0) THEN
                ack = ackermann_peter(m - 1, to_im(1))
            ELSE
                ack = ackermann_peter(m - 1, ackermann_peter(m, n - 1))
            END IF

            CALL FM_EXIT_USER_FUNCTION(ack)

        END FUNCTION

END PROGRAM ackermann
