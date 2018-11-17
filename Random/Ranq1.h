// Recommended generator for everyday use. The period is 1.8e19 .
// Adapted from Numerical Recepies 3rd Edition, Section 7.1.3
#include <stdint.h>

enum{
    A1      = 21,
    A2      = 35,
    A3      = 4,
    D1      = 2685821657736338717ULL,
    PRIME   = 4101842887655102017ULL
};

// 1/(2^64)
static const double MLTPLY  = 5.42101086242752217E-20;

// 1/(2^63)
static const double MLTPLY2  = 1.084202172485504434E-19;

// Initialise the random, stored value with a large prime
static uint64_t val = PRIME;

// Seed the RNG
void initRanq1( uint64_t j ){
    val ^= j;
}

// 64-bit, random integer
static uint64_t int64Ranq1(){
    val ^= val >> A1;
    val ^= val << A2;
    val ^= val >> A3;
    return val * D1;
}

// Uniform random numbers between 0.0 and 1.0
double dblRanq1(){ return MLTPLY * int64Ranq1(); }
// Uniform random numbers between -1.0 and 1.0
double dblRanq1Sym(){ return ((MLTPLY2 * int64Ranq1()) - 1.0); }

// 32-bit, random integer
static uint32_t int32Ranq1(){ return ( uint32_t )int64Ranq1(); }
