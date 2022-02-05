#include<stdio.h>
#include<math.h>
int main(){
    double H,S1,V,L,K;
    int n;
    scanf("%lf %lf %lf %lf %lf %d",&H,&S1,&V,&L,&K,&n);
    double t_top=sqrt((H-K-0.0001)/5),t_bot=sqrt(H/5);
    double left_end=S1-t_bot*V-0.0001,right_end=S1-t_top*V+L+0.0001;
    int right=right_end<n-1?(int)right_end:n-1;
    int left=left_end>=0?(int)left_end:-1;
    if(left>right)left=right;
    printf("%d",right-left);
    return 0;
}