#include<stdio.h> 
int a[1010],x,num,b[10]={0,1,2,3,5,10,20},ans,t[1010];
int main(){
    for(int i=1;i<=6;i++){
        scanf("%d",&x);
        for(int j=1;j<=x;j++)  a[++num]=b[i];
    }
    t[0]=1;
    for(int i=1;i<=num;i++)
        for(int j=1010;j>=0;j--)  if(t[j])  t[j+a[i]]=1;  
    for(int i=1;i<=1010;i++)  if(t[i])  ans++;
    printf("Total=%d",ans);
    return 0;
}
