#include<stdio.h>
#if area==1
int main(){
    int n;
    scanf("%d",&n);
    int kindn[n];
    for(int i=0;i<n;i++){
        scanf("%d",&kindn[i]);
        if(i>0&&kindn[i]==kindn[i-1])
            i--,n--;
    }
    int rest=2;
    if(n==1)rest=1;
    for(int i=1;i<n-1;i++)
        if(kindn[i-1]>kindn[i]&&kindn[i+1]>kindn[i]||
        kindn[i-1]<kindn[i]&&kindn[i+1]<kindn[i]){
            printf("%d\n",kindn[i]);
            rest++;
        }
    printf("%d",rest);
}