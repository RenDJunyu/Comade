#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main(){
    int n,base;
    scanf("%d %d",&n,&base);
    printf("%d=",n);
    int power=0;
    if(n>=0)while((-base-1)*(pow(base,power+2)-1)/(pow(base,2)-1)<n)power+=2;
    else {
        power++;
        while(base*(-base-1)*(pow(base,power+1)-1)/(pow(base,2)-1)>n)power+=2;
    }
    do{
        int factor=0;
        if(n>=0&&power%2==0)
            while(factor*pow(base,power)<n&&factor<-base-1){
                if((-base-1)*(pow(base,power)-1)/(pow(base,2)-1)+factor*pow(base,power)>=n)break;
                factor++;
            }
        else if(n<0&&power%2==1)
            while(factor*pow(base,power)>n&&factor<-base-1){
                if(base*(-base-1)*(pow(base,power-1)-1)/(pow(base,2)-1)+factor*pow(base,power)<=n)break;
                factor++;
            }
        if(factor<10)printf("%d",factor);
        else printf("%c",factor-10+'A');
        n-=factor*(int)pow(base,power);
    }while(power--!=0);
    printf("(base%d)",base);
}