#include<stdio.h>
int main()
{
	int a1,a2,a3,b1,b2,b3,c1,c2,c3,X;
	for(X=111;X<=333;X++)
	{
		a1=X/100;
		a2=(X-a1*100)/10;
		a3=X-a1*100-a2*10;
		b1=X*2/100;
		b2=(X*2-b1*100)/10;
		b3=X*2-b1*100-b2*10;
		c1=X*3/100;
		c2=(X*3-c1*100)/10;
		c3=X*3-c1*100-c2*10;
		if(
		a1!=a2&&a1!=a3&&a1!=b1&&a1!=b2&&a1!=b3&&a1!=c1&&a1!=c2&&a1!=c3&&
		a2!=a3&&a2!=b1&&a2!=b2&&a2!=b3&&a2!=c1&&a2!=c2&&a2!=c3&&
		a3!=b1&&a3!=b2&&a3!=b3&&a3!=c1&&a3!=c2&&a3!=c3&&
		b1!=b2&&b1!=b3&&b1!=c1&&b1!=c2&&b1!=c3&&
		b2!=b3&&b2!=c1&&b2!=c2&&b2!=c3&&
		b3!=c1&&b3!=c2&&b3!=c3&&
		c1!=c2&&c1!=c3&&
		c2!=c3&&
		a1+a2+a3+b1+b2+b3+c1+c2+c3==45)
		{
			printf("%d %d %d\n",X,X*2,X*3);
		}
	}
	scanf("\n") ;
	return 0;
}
