#include<stdio.h>
int main()
{
	int n,x,t,a=1;
	scanf("%d %d",&n,&x);
	for(t=0;a<=n;a++)
	{
		if(a/1%10==x)
		{
			t++;
		}
		if(a>9&&a/10%10==x)
		{
			t++;
		}
		if(a>99&&a/100%10==x)
		{
			t++;
		}
		if(a>999&&a/1000%10==x)
		{
			t++;
		}
		if(a>9999&&a/10000%10==x)
		{
			t++;
		}
		if(a>99999&&a/100000%10==x)
		{
			t++;
		}
		if(a>999999&&a/1000000%10==x)
		{
			t++;
		}
	}
	printf("%d",t);
	return 0;
 }
