## randoms.c

Prints random numbers from generators fed to it as header files. It currently uses the following:

* __ran1.h__: An RNG from the old Numerical Recipes
* __Ranq1.h__: A new RNG from the latest Numerical Recipes
* __random__: The POSIX random number source. (This is used directly in randoms.c)

## dev_random.f90

Reads bit streams from random number sources and tests for the probability of `1`s.
