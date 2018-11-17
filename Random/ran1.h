#include <float.h>

enum{
	IA      = 16807,
	IM      = 2147483647,
	IQ      = 127773,
	IR      = 2836,
	NTAB    = 32,
	NDIV    = (1+(IM-1)/NTAB),
};

static const double AM      = 1.0/IM;
static const double RNMX    = 1.0 - DBL_EPSILON;
static const double EPS     = 3.0e-7;
static const double FPMIN   = 1.0e-30;

double ran1(int *idum){
	int j;
	int k;
	static int iy=0;
	static int iv[NTAB];
	double temp;

	if ( *idum <= 0 || !iy) {
		if (-(*idum) < 1) *idum=1;
		else *idum = -(*idum);
		for (j=NTAB+7;j>=0;j--) {
			k = *idum/IQ;
			*idum=IA*(*idum-k*IQ)-IR*k;
			if (*idum < 0) *idum += IM;
			if (j < NTAB) iv[j] = *idum;
		}
		iy=iv[0];
	}
	k=*idum/IQ;
	*idum=IA*(*idum-k*IQ)-IR*k;
	if (*idum < 0) *idum += IM;
	j=iy/NDIV;
	iy=iv[j];
	iv[j] = *idum;
	if ((temp=AM*iy) > RNMX) return RNMX;
	else return temp;
}

