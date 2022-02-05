#include<stdio.h>
int main(){
	int M,N;
	scanf("%d %d",&M,&N);
	int i,p,q,r=0,W[100],w,n=0;
	for(i=0;i<M;i++)W[i]=-1;
	for(i=0;i<N;i++){
		scanf("%d",&w),q=1;
		for(p=0;p<M;p++){//检索 
			if(w==W[p]){
				q--;break;
			}		
		}
		if(q==0)continue;//内存中存在则跳过 
		else{
			W[r]=w;n++;r++;
			if(r==M)r=0;//否则进行存储，注意，这里巧妙地实现了先进先出 
		}
	}
	printf("%d",n);
	return 0;
}
