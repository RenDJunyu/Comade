#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int kindn[n];
    for(int i=0;i<n;i++)
        scanf("%d",&kindn[i]);
    int usage=0;
    while(n>1){
        int low1=0,low2=1;
        if(kindn[low1]>kindn[low2]){
            low2+=low1;
            low1=low2-low1;
            low2-=low1;
        }
        for(int i=2;i<n;i++)
            if(kindn[i]<kindn[low1]){
                low2=low1;
                low1=i;
            }
            else if(kindn[i]<kindn[low2])
                low2=i;
        kindn[low1]+=kindn[low2];
        usage+=kindn[low1];
        kindn[low2]=kindn[--n];
    }
    printf("%d",usage);
}