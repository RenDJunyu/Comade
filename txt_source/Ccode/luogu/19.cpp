#include<stdio.h>
int main()
{
	char h[6],d[6],a[28]="0ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	int n1=1,n2=1,i,p;
	scanf("%s %s",h,d);
	for(i=0;i<=5;i++)
	{
		if(h[i]==0)
		continue;
		for(p=1;p<=26;p++)
		{
			if(h[i]==a[p])
			{
				n1*=p;
			    break;
			}
		}
	}
	for(i=0;i<=5;i++)
	{
		if(d[i]==0)
		continue;
		for(p=1;p<=26;p++)
		{
			if(d[i]==a[p])
			{
				n2*=p;
				break;
			}
		}
	}
	if(n1%47==n2%47)
		printf("GO");
	else
		printf("STAY");
	return 0;
}
