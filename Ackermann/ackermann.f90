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
