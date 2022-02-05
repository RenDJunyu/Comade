#include<stdio.h>
int main()
{
	int L,M,n,N=0,i;
	scanf("%d %d\n",&L,&M);
	int a[200],b[10001];
	for(i=0;i<=L;i++)
	{
		b[i]=i;
	}
	for(n=1;n<=M;n++)
	{
		scanf("%d %d",&a[n*2-2],&a[n*2-1]);
		for(i=0;i<=L-1;i++)
		{
			if(b[i]>=a[n*2-2]&&b[i]<=a[n*2-1])
			{
				N++;
				b[i]=L+1;
			}
		}
	}
	printf("%d",L+1-N);
	return 0;
}
