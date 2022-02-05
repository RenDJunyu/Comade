#include<stdio.h>
int main()
{
	char N[11];
	scanf("%s",N);
	if(N[0]=='-')printf("-");
	for(int i=10;i>=0;i--)
	{
		if(N[i]>48)
		{
			for(;i>=0;i--)
			{
				if(N[i]=='-')return 0;
				printf("%c",N[i]);
			}
		}
	}	
	return 0;	
}
