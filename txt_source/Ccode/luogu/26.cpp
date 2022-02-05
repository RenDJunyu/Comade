#include<stdio.h>
int f(int n)
{
	int N[10]={6,2,5,5,4,5,6,3,7,6},p,m,i,t=0;
	for(i=0;i<1000;i++)
	{
		for(p=0;p<1000;p++)
		{
			m=N[i%10]+N[p%10]+N[(i+p)%10]+4;
			if(i>=10)m+=N[i%100/10];
			if(p>=10)m+=N[p%100/10];
			if(i+p>=10)m+=N[(i+p)%100/10];
			if(i>=100)m+=N[i/100];
			if(p>=100)m+=N[p/100];
			if(i+p>=100)m+=N[(i+p)/100];
			if(m==n)t++;
		}
	}
	return t;
} 
int main()
{
	int n;
	scanf("%d",&n);
	printf("%d",f(n));
	return 0;
}
