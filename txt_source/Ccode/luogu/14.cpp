#include<stdio.h>
int main()
{
	int a[100],i,p;
	for(i=0;i<=99;i++)
	{
		scanf("%d",&a[i]);
		if(a[i]==0)
		{
			for(p=i-1;p>=0;p--)
			{
				printf("%d ",a[p]);
			}
		return 0;
		}
	}	
}
