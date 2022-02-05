#include<stdio.h>
int f(int x)
{
	if(x==1)
	return 1;
	if(x==2)
	return 2;
	if(x/2*2==x)
	return f(x-1)+f(x/2);
	if(x/2*2==x-1)
	return f(x-1);
}
int main()
{
	int n,i,a[1000];
	scanf("%d",&n);
	printf("%d",f(n));
	return 0;
}
