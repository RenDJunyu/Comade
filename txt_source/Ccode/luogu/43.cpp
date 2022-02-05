#include<stdio.h>
int min(int a,int b){
	return a<b?a:b;
}
int main(){
	int M,N,K,L,D,XY[4000][2]={0},HL[1000][2]={0},hl[1000][2]={0};
	scanf("%d %d %d %d %d",&M,&N,&K,&L,&D);
	int i,p,m=0,n=0;
	D*=2;
	for(i=0;i<D;i++)scanf("%d %d",&XY[i][0],&XY[i][1]);
	for(i=0;i<D;i+=2){
		if(XY[i][0]!=XY[i+1][0])
		HL[min(XY[i][0],XY[i+1][0])-1][0]++;
		else HL[min(XY[i][1],XY[i+1][1])-1][1]++;
	}
	for(i=M-1;i>=1;i--){
		for(p=0;p<M-1;p++){
			if(HL[p][0]==i){
				if(m==K)break;
				if(p==0)hl[p][0]=p-1;
				else hl[p][0]=p;
				m++;	
			}
		}
	}
	for(i=N-1;i>=1;i--){
		for(p=0;p<N-1;p++){
			if(HL[p][1]==i){
				if(n==L)break;
				if(p==0)hl[p][1]=p-1;
				else hl[p][1]=p;
				n++;
			}
		}
	}
	for(i=0;i<M;i++)
	if(hl[i][0]!=0)printf("%d ",i+1);
	putchar('\n');
	for(i=0;i<N;i++)
	if(hl[i][1]!=0)printf("%d ",i+1);
	return 0;
}
