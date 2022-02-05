#include<stdio.h>
int main(){
    int N,Na,Nb;
    scanf("%d %d %d",&N,&Na,&Nb);
    int A[200]={0},B[200]={0},bj[5][5]={0},i,a=0,b=0;
    bj[0][1]=1,bj[0][4]=1,bj[1][2]=1,bj[1][4]=1,bj[2][0]=1,
    bj[2][3]=1,bj[3][0]=1,bj[3][1]=1,bj[4][2]=1,bj[4][3]=1;
    for(i=0;i<Na;i++){
        scanf("%d",&A[i]);
    }
    for(i=0;i<Nb;i++){
        scanf("%d",&B[i]);
    }
    for(i=0;i<N;i++){
        a+=(bj[A[i%Na]][B[i%Nb]]==0&&A[i%Na]!=B[i%Nb]),
        b+=(bj[A[i%Na]][B[i%Nb]]==1);
    }
    printf("%d %d",a,b);
    return 0;
}
