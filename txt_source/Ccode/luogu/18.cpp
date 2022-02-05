#include<stdio.h>
int main()
{
	char a[14],b[12]="0123456789X";
	int i,t=1,M=0;
	scanf("%s",a);
	for(i=0;i<=11;i++)
	{
		if(a[i]=='-')
		{
			continue;
		}
		M+=(a[i]-'0')*t++;
	}
	if(b[M%11]==a[12])
	{
		printf("Right");
	}
	else
	{
		a[12]=b[M%11];
		printf("%s",a);
	}
	return 0;
}
