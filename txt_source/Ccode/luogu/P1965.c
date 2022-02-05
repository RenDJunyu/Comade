#include<stdio.h>
#include<math.h>
int quick_exp(int num,int exp,int mod);
int main(){
	int n,m,k,x;
	scanf("%d %d %d %d",&n,&m,&k,&x);
	printf("%d",(x+m*quick_exp(10,k,n)%n)%n);
	return 0;
}
int quick_exp(int num,int exp,int mod){
    if(exp==0)return 1;
    else if(exp==1)return num;
    int backn=num,i=2;
    while(i<=exp){
        backn=backn*backn%mod;
        if(i*i>exp)break;
        i*=2;
    }
    return backn*quick_exp(num,exp-i,mod)%mod;
}