#include<stdio.h>
int main()
{
	int r,p=0,s=0,m=1;
	for(r=0;m<=12;m++)
	{
		scanf("%d",&p);
		r+=300-p;
		if(r<0)
		{
			printf("%d",-m);
			return 0;
		}
		s+=(r/100)*100;
		r%=100;
	}
	s=s*1.2+r;
	printf("%d",s);
	return 0;
}  
