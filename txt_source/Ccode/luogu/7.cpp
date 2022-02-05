#include<stdio.h>
int main()
{
	double N1,N2;
	for(N1=23;N1>=23;N1=N1*10+3)
	{
		for(N2=2;N2<N1;N2++)
		{
			if(N1%N2==0)
			{
				printf("%d\n",N1);
				N2=N1;
			}
		}
	}
	return 0;
 } 
