#include<stdio.h>
#include<stdlib.h>
int main(){
    int a,b;
    scanf("%d %d",&a,&b);
    if(a>b){
        a=a+b;
        b=a-b;
        a=a-b;
    }
    int *can_make=(int *)malloc(sizeof(int)),size=1;
    can_make[0]=0;
    for(int i=a-1,count=0;count<a;i++){
        int p=-1;
        while(++p<size)
            if(can_make[p]+a==i||can_make[p]+b==i){
                can_make=(int *)realloc(can_make,sizeof(int)*(size+1));
                can_make[size++]=i;
                count++;
                break;
            }
        if(p==size)count=0;
    }
    printf("%d",can_make[size-a]-1);
}