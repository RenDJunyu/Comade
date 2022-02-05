#include<stdio.h>
long long A[25][25][25];
long long w(long long a,long long b,long long c)
{
    if(a<=0||b<=0||c<=0)return 1;
    if(A[a][b][c]!=0)return A[a][b][c];
    if(a<b&&b<c)A[a][b][c]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c);
    else A[a][b][c]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1);
    return A[a][b][c];
}
int main()
{
	long long a,b,c;
	for(;;)
	{
		scanf("%lld %lld %lld",&a,&b,&c);
		if(a==-1&&b==-1&&c==-1)
		return 0;
		printf("w(%lld, %lld, %lld) = ",a,b,c);
		if(a>20||b>20||c>20)
		{
			if(a>0&&b>0&&c>0)
			{
				a=20,b=20,c=20;
			}
		}
    	printf("%lld\n",w(a,b,c));
	}	
}
