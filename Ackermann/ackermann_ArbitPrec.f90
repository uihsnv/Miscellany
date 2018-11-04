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
