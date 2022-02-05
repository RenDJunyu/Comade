/*这个题思路
    求最长升、最长降序列
*/
#include<stdio.h>
#define max(a,b) (a)>(b)?(a):(b)
int main(){
    int n,height[105],list[2][105]={0},ans;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&height[i]);
    height[0]=0;
    for(int i=1;i<=n;i++)
        for(int j=0;j<i;j++) 
            if(height[i]>height[j])
                list[0][i]=max(list[0][i],list[0][j]+1);
    height[n+1]=0;
    for(int i=n;i;i--) 
        for(int j=n+1;j>i;j--)
            if(height[i]>height[j])
                list[1][i]=max(list[1][i],list[1][j]+1);
    for(int i=1;i<=n;i++)
        ans=max(list[0][i]+list[1][i]-1,ans);
    printf("%d\n",n-ans);
    return 0;
}