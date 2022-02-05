#include<stdio.h>
int main()
{
	int a,b,k,n,m;
    scanf("%d %d %d %d %d",&a,&b,&k,&n,&m);
    a=a%10007;
    b=b%10007;
    //ab取模
    int operatee=1;
    for(int i=k-n+1;i<=k;i++)
        operatee=operatee*i%10007;
    for(int p=0;p<10005;p++)
        for(int i=1;i<=n;i++)
            operatee=operatee*i%10007;
    //组合
    for(int i=1;i<=n;i++)
        operatee=operatee*a%10007;
    //计算a系数
    for(int i=1;i<=m;i++)
        operatee=operatee*b%10007;
    //计算b系数
    printf("%d",operatee);
}