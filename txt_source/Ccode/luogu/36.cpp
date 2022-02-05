#include<stdio.h>
int main()
{
	int N,i;
	scanf("%d",&N);
	for(i=1;;i++)
	{
		N-=i;
		if(N<=0)break;
	}
	N+=i;
	printf("%d/%d",(i%2==1)*(i+1-N)+(i%2==0)*N,i+1-(i%2==1)*(i+1-N)-(i%2==0)*N);
	return 0;
 } 
