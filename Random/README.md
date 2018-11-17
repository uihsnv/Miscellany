##randoms.c

Prints random numbers from generators fed to it as header files. It currently uses the following:

* _ran1.h_: An RNG from the old Numerical Recipes
* _Ranq1.h_: A new RNG from the latest Numerical Recipes
* _random_: The POSIX random number source. (This is used directly in randoms.c)

##dev_random.f90

Reads bit streams from random number sources and tests for the probability of `1`s.
