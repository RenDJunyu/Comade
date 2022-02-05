#include<stdio.h>
int main()
{
	int n,i,q,N,a[100];
	scanf("%d\n",&n);
	for(i=0;i<=n-1;i++)
	{
		scanf("%d",&a[i]);
		for(q=0,N=0;q<i;q++)
		{
			if(a[i]>a[q])
			{
				N++;
			}
		}
		printf("%d ",N);
	}
	return 0;
 } 
