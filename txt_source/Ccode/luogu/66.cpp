#include<stdio.h>
int tear(int N,int K,int *T,int form){
	if(K==1){
		if(N>=form)(*T)++;
		return 0;
	}
	for(int i=form;i<=N-K;i++)
		tear(N-i,K-1,T,i);
}
int main(){
	int n,k;
	scanf("%d %d",&n,&k);
	int t=0,i;
	for(i=1;i<=n-k;i++)
		tear(n-i,k-1,&t,i);
	printf("%d",t);
	return 0; 
}
