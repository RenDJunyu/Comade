#include<stdio.h>
#include<math.h>
int main()
{
	double a,b,c;
	scanf("%lf %lf %lf",&a,&b,&c);
	if(a==0&&b==0&&c!=0)
	printf("Not An Equation");
	else if(a==0&&b==0&&c==0)
	printf("Zero Equation");
	else if(a==0&&c==0)
	printf("%.2lf",0);
	else if(a==0)printf("%.2lf",-c/b);
	else if(b*b-4*a*c==0)
	{
		if(b/(2*a)==0)
		printf("%.2lf",0);
		else printf("%.2lf",-b/(2*a));
	}
	else if(b*b-4*a*c>0)
	{
		if(a<0)a*=-1,b*=-1,c*=-1;
		if(c==0)
		{
			if(a*b<0)printf("%.2lf\n%.2lf",-b/a,0);
			else if(a*b>0)printf("%.2lf\n%.2lf",0,-b/a); 
		}
		else printf("%.2lf\n%.2lf",(-b+pow(b*b-4*a*c,0.5))/(2*a),(-b-pow(b*b-4*a*c,0.5))/(2*a));
	}
	else if(b*b-4*a*c<0)
	{
		if(b/(2*a)==0)
		printf("0.00+%.2lfi\n0.00%.2lfi",pow(c/a,0.5),-pow(c/a,0.5));
		else printf("%.2lf+%.2lfi\n%.2lf%.2lfi",-b/(2*a),pow(c/a-b*b/(4*a*a),0.5),-b/(2*a),-pow(c/a-b*b/(4*a*a),0.5));
	}
	return 0;
 } 
