#include<stdio.h>
#include<math.h>
int k,a[20],n,i;
int kg(int n)
{
    int s=sqrt(n);
    for(int i=2;i<=s;i++)
	{
		if(n%i==0)
    	return 0;
    }
    return 1;
}
int f(int k,int h,int s,int n)
{
	if(k==0)
	{
		return kg(h);
	}
	int sum=0;
	for(int i=s;i<=n;i++)
	{
		sum+=f(k-1,h+a[i],i+1,n);
	}
	return sum;
}
int main()
{
	scanf("%d %d",&n,&k);
	for(int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("%d",f(k,0,0,n-1));
	return 0;
}
