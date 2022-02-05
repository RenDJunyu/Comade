#include<stdio.h>
int main()
{
	double L,S,N=0;
	scanf("%lf",&L);
	for(S=2;L>=0;S*=0.98)
	{
		L-=S;
		N++;
	}
	printf("%.0lf",N);
	return 0; 
 } 
