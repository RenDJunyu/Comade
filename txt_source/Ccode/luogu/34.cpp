#include<stdio.h>
int main()
{
	double v=7,l=0;
	int s,x;
	scanf("%d %d",&s,&x);
	for(int i=1;i<20;i++)
	{
		
		if(l>=s-x&&l<s+x&&l+v<=s+x)
		{
			printf("y");
			return 0;
		}
		if(l>=s-x&&l<s+x&&l+v>s+x)
		{
			printf("n");
			return 0;
		}
		l+=v;v*=0.98;
	}
} 
