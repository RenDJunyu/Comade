/*此题核心部分
    推导算式
    Σ_l=1^nΣ_r=l^nS(l,r)
    =(n+1)*Σ_i=1^npreai*prebi-Σ_i=1^npreai*Σ_i=1^nprebi
*/
#include<stdio.h>
const int mod=1e9+7;
void get_pres(long long *out,int figure);
void get_result(int figure,long long *preai,long long *prebi);
int main(){
    int n;
    scanf("%d",&n);
    long long preai[n],prebi[n];
    get_pres(preai,n);
    get_pres(prebi,n);
    get_result(n,preai,prebi);
    return 0;
}
void get_pres(long long *out,int figure){
    int num;
    for(int i=0;i<figure;i++){
        scanf("%d",&num);
        if(i==0)*(out+i)=num%mod;
        else *(out+i)=(*(out+i-1)+num)%mod;
    }
}
void get_result(int figure,long long *preai,long long *prebi){
    long long result=0,tmpa=0,tmpb=0;
    for(int i=0;i<figure;i++){
        result=(result+(figure+1)**(preai+i)%mod**(prebi+i)%mod)%mod;
        tmpa=(tmpa+*(preai+i))%mod;
        tmpb=(tmpb+*(prebi+i))%mod;
    }
    result=(result-tmpa*tmpb%mod+mod)%mod;
    printf("%lld",result);
}