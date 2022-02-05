#include<stdio.h>
int main()
{
	int D=0,i,M[12]={31,28,31,30,31,30,31,31,30,31,30,31};
	int m1,d1,m2,d2;
	scanf("%d:%d %d:%d",&m1,&d1,&m2,&d2);
	for(i=m1-1;i<m2-1;i++)
	{
		D+=M[i];
	}
	D+=d2-d1;
	if(m1>m2)D=-D;
	if(m1==m2&&d1>d2)D=-D;
	printf("%d",D);
	return 0;
}
