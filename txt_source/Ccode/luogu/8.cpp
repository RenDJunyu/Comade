#include<stdio.h>
int main()
{
	double K,N,S=0;
	scanf("%lf",&K);
	for(N=1;S<=K;N++)
	{
		S=S+1/N;
	}
	N--;
	printf("%.0lf",N);
	return 0;
 }
