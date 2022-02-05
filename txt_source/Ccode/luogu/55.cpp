#include<stdio.h>
int main(){
	int a,n,m,x;
	int i,num=0,fiba[18]={1,0},fibx[18]={0,1};
	scanf("%d %d %d %d",&a,&n,&m,&x);
	for(i=0;i<16;i++){
		fiba[i+2]=fiba[i+1]+fiba[i];
		fibx[i+2]=fibx[i+1]+fibx[i];
		if(i>0){
			fiba[i]+=fiba[i-1];
			fibx[i]+=fibx[i-1];
		}
	}
	fiba[16]+=fiba[15],fiba[17]+=fiba[16];
	fibx[16]+=fibx[15],fibx[17]+=fibx[16];
	num=(m-a*(1+fiba[n-4]))/fibx[n-4];
	if(x==2)printf("%d",a);
	else printf("%d",a*(1+fiba[x-3])+num*fibx[x-3]);
	return 0;
}
