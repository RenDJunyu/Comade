#include<stdio.h>
int main()
{
	int a[10],b,n=0,i;
	scanf("%d %d %d %d %d %d %d %d %d %d\n%d",
	&a[0],&a[1],&a[2],&a[3],&a[4],&a[5],&a[6],&a[7],&a[8],&a[9],&b);
	for(i=0;i<=9;i++)
	{
		if(b+30>=a[i])
		{
			n++;
		}
	}
	printf("%d",n);
	return 0;
}
