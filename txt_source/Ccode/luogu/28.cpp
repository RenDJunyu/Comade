#include<stdio.h>
int main()
{
	int n,s,a,b;
	scanf("%d %d %d %d",&n,&s,&a,&b);
	int i,N[5000][2],p,t=0;
	for(i=0;i<n;i++)
	{
		scanf("%d %d",&N[i][0],&N[i][1]);
	}
	for(p=0;p<=100;p++)
	{
		for(i=0;i<n;i++)
		{
			if(p==N[i][1]&&N[i][0]<=a+b&&s>=N[i][1])
			{
				s-=N[i][1];
				t++;
			}
		}
	}
	printf("%d",t);
	return 0;
}
