#include<stdio.h>
int main()
{
	int s,a,d;
	for(d=1;d<=7;d++)
	{
		scanf("%d %d",&s,&a);
		if(s+a>8)
		{
			printf("%d",d);
			return 0;
		}
	}
	printf("0");
	return 0;
}
