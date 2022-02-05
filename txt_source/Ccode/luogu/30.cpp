#include<stdio.h>
int main()
{
	int A,B,C;
	int i,p,q,X,Y,Z,a[9],b[9],m,n,t,T=0;
	scanf("%d %d %d",&A,&B,&C);
	for(i=1;i<=3;i++)
	{
		for(p=1;p<=9;p++)
		{
			if(p==i)continue;
			for(q=1;q<=9;q++)
			{
				if(q==i||q==p)
				continue;
				X=i*100+p*10+q;
				if(X%A!=0)continue;
				Y=X/A*B;
				Z=X/A*C;
				if(Z>999)continue;
				t=0;
				for(m=0;m<=8;m++)b[m]=m+1;
				a[0]=i;a[1]=p;a[2]=q;
				a[3]=Y/100;a[4]=Y%100/10;a[5]=Y%10;
				a[6]=Z/100;a[7]=Z%100/10;a[8]=Z%10;
				for(m=0;m<=8;m++)
				{
					for(n=0;n<=8;n++)
					{
						if(a[m]==b[n])
						{
							t++;
							b[n]=10;
						}
					}
				}
				if(t==9)
				{
					T++;
					printf("%d %d %d\n",X,Y,Z);
				}		
			}
		}
	}
	if(T==0)printf("No!!!");
	return 0;
}
