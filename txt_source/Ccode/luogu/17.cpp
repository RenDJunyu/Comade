#include<stdio.h>
int max(int a,int b)
{
	return a>b?a:b;
	
}
int main()
{
	int a[2],N,n=0,i,d=0,D=1;
	scanf("%d",&N);
	a[1]=-1;
	for (i=1;n<N;n++)
	{
		i--;
		scanf("%d",&a[i]);
		n++;
		if(n>=N)
		{
			break;
		}
		if(a[0]<=a[1])
		{
			D=max(D,d);
			d=1;
		}
		else
		{
			d++;
		}
		i++;
		scanf("%d",&a[i]);
		n++;
		if(n>=N)
		{
			break;
		}
		if(a[1]<=a[0])
		{
			D=max(D,d);
			d=1;
		}
		else
		{
			d++;
		}
		i--;
		scanf("%d",&a[i]);
		n++;
		if(n>=N)
		{
			break;
		}
		if(a[0]<=a[1])
		{
			D=max(D,d);
			d=1;
		}
		else
		{
			d++;
		}
		i++;
		scanf("%d",&a[i]);
		if(a[1]<=a[0])
		{
			D=max(D,d);
			d=1;
		}
		else
		{
			d++;
		}
	 } 
	 printf("%d",D);
	 return 0;
 } 
