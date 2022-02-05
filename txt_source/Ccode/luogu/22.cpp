#include<stdio.h>
int max(int a,int b)
{
	return a>b?a:b; 
}
int main()
{
	int a[27]={0},b[27],t,h=0,n,i;
	char l[27]="ABCDEFGHIJKLMNOPQRSTUVWXYZ",w[101]="\0";
	for(t=0;t<=3;t++)
	{
		gets(w);
		for(i=0;i<=99;i++)
		{
			for(n=0;n<=25;n++)
			{
				if(w[i]==l[n])
				{
					a[n]++;
				}		
			}
		}
		for(i=0;i<=99;i++)
		{
			w[i]='\0';
		}
	}
	for(t=a[0],i=1;i<=25;i++)
	{
		t=max(t,a[i]);
	}
	for(i=0;i<=t-1;i++)
	{
		for(h=25;h>=0;h--)
		{
			if(t-a[h]<=i)
			{
				b[i]=h;
				break;
			}
		}
	}
	for(i=0;i<=t-1;i++)
	{
		for(h=0;h<=25;h++)
		{
			if(t-a[h]<=i&&h!=b[i])
			{
				printf("* ");
			}
			if(t-a[h]>i)
			{
				printf("  ");
			}
			if(h==b[i])
			{
				printf("*\n");
				h=25;
			}
		}
	}
	printf("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z");
	return 0;
}
