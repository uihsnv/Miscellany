#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <float.h>
#include "ran1.h"
#include "Ranq1.h"

#define UNI01               ((double)random()/((double)RAND_MAX + 1.0))
#define UNIm11              ((2.0*UNI)-1.0)

enum { NR_ran1, NR_Ranq1, POSIX_random } RNG;

static unsigned long long serial;
static int for_ran1;

int main( int n, char **inputStrings ){

    unsigned long long seed;
    unsigned int i;
    char randFileName[32];
    FILE *randFile;

    if (n != 2){
        printf("Please append one integer to the executable\n");
        exit(EXIT_FAILURE);
    }

    // Set the random number generator
    // Choose from: NR_ran1, NR_Ranq1 and POSIX_random
    //RNG = NR_ran1;
    RNG = NR_Ranq1;
    //RNG = POSIX_random;

    sscanf(inputStrings[1],"%llu",&serial);
    seed = (unsigned long long)time(0) + serial;

    // Seed the rng
    switch(RNG){
        case NR_ran1: for_ran1 = -(int)seed; ran1(&for_ran1); break;
        case NR_Ranq1: initRanq1(seed); break;
        case POSIX_random: srandom((unsigned int)seed); break;
    }

    //sprintf(randFileName,"randNums.dat");
    //randFile = fopen(randFileName,"a");

    for (i=0; i<5; i++){
        switch(RNG){
            case NR_ran1: printf( "%0.*f\n", DBL_DIG, ran1(&for_ran1) ); break;
            case NR_Ranq1: printf( "%0.*f\n", DBL_DIG, dblRanq1() ); break;
            case POSIX_random: printf( "%0.*f\n", DBL_DIG, UNI01 ); break;
        }
        //fprintf(randFile,"%0.*f\n",DBL_DIG,dblRanq1());
    }
    printf("\n");

}
