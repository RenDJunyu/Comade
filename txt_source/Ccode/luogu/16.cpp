#include<stdio.h>
int main()
{
	int n,N=0,i,q=0,p,a[100],b[10000];
	scanf("%d\n",&n);
	for(i=0;i<=n-1;i++)
	{
		scanf("%d",&a[i]);
		for(p=0;p<i;p++,q++)
		{
			b[q]=a[i]+a[p];
		}
	}
	for(i=0;i<=n-1;i++)
	{
		for(p=0;p<=q-1;p++)
		{
			if(a[i]==b[p])
			{
				N++;
				break;
			}
		}
	}
	printf("%d",N);
	return 0;
 } 
