#include<stdio.h>
int main()
{
	double u,p;
	scanf("%lf",&u);
	if(u<=150)
	{
		p=u*0.4463;
	}
	else if(u>=150&&u<=400)
	{
		p=0.4463*150+0.4663*(u-150);
	}
	else if(u>=401)
	{
		p=0.4463*150+0.4663*(400-150)+0.5663*(u-400);
	}
	printf("%.1lf",p);
	return 0;
 } 
