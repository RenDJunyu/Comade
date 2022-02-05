#include<stdio.h>
#include<math.h>
int ss(int n)
{
	if(n==2||n==3)return 1;
	for(int i=2;i<=sqrt(n);i++)
	{
		if(n%i==0)return 0;
	}
	return 1;
}
int main()
{
	int N,i,p,q,n[20000],t=0;
	scanf("%d",&N);
	for(i=2;i<20000;i++)
	{
		if(ss(i)==1)
		{
			n[t]=i;
			t++;
		}
	}
	for(i=0;i<t;i++)
	{
		for(p=0;p<t;p++)
		{
			for(q=0;q<t;q++)
			{
				if(n[i]+n[p]+n[q]==N)
				{
					printf("%d %d %d",n[i],n[p],n[q]);
					return 0;
				}
			}
		}
	}
}
