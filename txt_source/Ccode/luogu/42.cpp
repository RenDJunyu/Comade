#include<stdio.h>
int main(){
	int M,N;
	scanf("%d %d",&M,&N);
	int i,p,q,r=0,W[100],w,n=0;
	for(i=0;i<M;i++)W[i]=-1;
	for(i=0;i<N;i++){
		scanf("%d",&w),q=1;
		for(p=0;p<M;p++){//���� 
			if(w==W[p]){
				q--;break;
			}		
		}
		if(q==0)continue;//�ڴ��д��������� 
		else{
			W[r]=w;n++;r++;
			if(r==M)r=0;//������д洢��ע�⣬���������ʵ�����Ƚ��ȳ� 
		}
	}
	printf("%d",n);
	return 0;
}
