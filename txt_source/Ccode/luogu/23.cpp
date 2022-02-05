#include<stdio.h>
int main()
{
	char a[53]="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",m[50]="\0";
	int n,i,t;
	scanf("%d %s",&n,m);
	n%=26;
	for(i=0;i<=49;i++)
	{
		if(m[i]=='\0')
		{
			i=49;
			continue;
		}
		for(t=0;t<=25;t++)
		{
			if(m[i]==a[t])
			{
				m[i]=a[t+n];
				break;
			} 
		} 
	}
	printf("%s",m);
	return 0;
}
