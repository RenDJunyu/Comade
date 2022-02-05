#include<stdio.h>
int main()
{
	int x,n,t=0;
	scanf("%d %d",&x,&n);
	if(x<=6&&x+n%7-1>=6)
	{
		t++;
	}
	if(x<=7&&x+n%7-1>=7)
	{
		t++;
	}
	if(x<=13&&x+n%7-1>=13)
	{
		t++;
	}
	if(x<=14&&x+n%7-1>=14)
	{
		t++;
	}
	printf("%d",(n/7*5+n%7-t)*250);
	return 0;
}
