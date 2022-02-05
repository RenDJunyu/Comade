#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<stdbool.h>
void get_cellar(int *cellar[],int N);
void find_way(int *cellar[],int N,int step,int way[N]);
int main(){
    int N;
    scanf("%d",&N);
    int *cellar[N],way[N];
    get_cellar(cellar,N);
    find_way(cellar,N,0,way);
    return 0;
}
void get_cellar(int *cellar[],int N){
    for(int i=0;i<N;i++){
        cellar[i]=(int *)malloc(sizeof(int)*(N-i));
        for(int j=0;j<N-i;j++)
            scanf("%d",&cellar[i][j]);
    }
}
void find_way(int *cellar[],int N,int step,int way[N]){
    static int real_way[20]={0};
    static int backn=0;
    bool sign_out=false;
    if(step==0){
        for(int i=1;i<=N;i++){
            way[step]=i;
            find_way(cellar,N,step+1,way);
        }
        for(int i=0;i<N&&real_way[i]!=0;i++){
            if(i>0)putchar(' ');
            printf("%d",real_way[i]);
        }
        printf("\n%d",backn);
    }
    else {
        for(int i=way[step-1];i<=N;i++)
            if(i!=way[step-1]&&cellar[i>way[step-1]?way[step-1]:i][abs(i-way[step-1])-1]){
                int j=-1;
                while(++j<step)
                    if(i==way[j])break;
                if(j==step){
                    way[step]=i;
                    find_way(cellar,N,step+1,way);
                    sign_out=true;
                }
            }
        if(!sign_out){
            int census=0;
            for(int i=0;i<step;i++)
                census+=cellar[0][way[i]-1];
            if(census>backn){
                backn=census;
                for(int i=0;i<step;i++)
                    real_way[i]=way[i];
                if(step<20)real_way[step]=0;
            }
        }
    }
}