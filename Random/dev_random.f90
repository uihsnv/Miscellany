PROGRAM dev_random

    INTEGER, PARAMETER :: n = 1000
    INTEGER, DIMENSION(n) :: randoms
    INTEGER :: un, istat, i, c, bits_per_int

    OPEN(NEWUNIT=un, FILE="/dev/urandom", ACCESS="stream", FORM="unformatted", ACTION="read", STATUS="old", IOSTAT=istat)
    !OPEN(NEWUNIT=un, FILE="/dev/ttyACM0", ACCESS="stream", FORM="unformatted", ACTION="read", STATUS="old", IOSTAT=istat)
    !OPEN(NEWUNIT=un, FILE="/home/user1/Temporary/randoms2", ACCESS="stream", FORM="unformatted", ACTION="read", STATUS="old", IOSTAT=istat)

    IF (istat .NE. 0) ERROR STOP "Unsuccessful device access"

    READ(un) randoms
    CLOSE(un)

    bits_per_int = BIT_SIZE(randoms)
    c = 0
    DO i = 1, bits_per_int
        c = c + COUNT(BTEST(randoms, i))
    END DO

    PRINT*, c/REAL(bits_per_int*n)

END PROGRAM dev_random
