#include<stdio.h>
int main(){
	int pre,prsa[100000][2]={0},dopr,dipr,Pre=0,t,masa=0,ifa=0;
	scanf("%d",&pre);
	int i,p,q;
	for(i=0;prsa[i-1][0]!=-1;i++){
		scanf("%d %d",&prsa[i][0],&prsa[i][1]);
		if(prsa[i][0]==pre)Pre=i;
	}
	i--;prsa[i][0]=0;prsa[i][1]=0;
	scanf("%d",&dopr);
	if(prsa[i-1][0]>pre&&Pre==0){
		for(i=1;prsa[i-1][1]>0;i++){
			prsa[i][0]=prsa[i-1][0]+1;
			prsa[i][1]=prsa[i-1][1]-dopr;
			if(prsa[i][0]==pre)Pre=i;
		}	
	}
	for(;prsa[i-1][1]>0;i++){
		prsa[i][0]=prsa[i-1][0]+1;
		prsa[i][1]=prsa[i-1][1]-dopr;
		if(prsa[i][0]==pre)Pre=i;
	}
	prsa[i-1][0]=0;prsa[i-1][1]=0;t=i-2;
	for(i=1;i<=t;i++){
		prsa[i][0]-=prsa[0][0];
	}
	pre-=prsa[0][0];
	prsa[0][0]=0;
	for(p=0;p<(prsa[t][0]+pre);p++){
		for(masa=0,q=0;q<=t;q++){
			masa=masa>((prsa[q][0]+p)*prsa[q][1])?masa:((prsa[q][0]+p)*prsa[q][1]);
		}
		if(masa==((prsa[Pre][0]+p)*prsa[Pre][1])){
			dipr=p;break;
		}
	}
	if(p==(prsa[t][0]+pre)){
		ifa++;dipr=prsa[t][0];
	}
	for(p=-1;p>-dipr;p--){
		for(masa=0,q=0;q<=t;q++){
			masa=masa>((prsa[q][0]+p)*prsa[q][1])?masa:((prsa[q][0]+p)*prsa[q][1]);
		}
		if(masa==((prsa[Pre][0]+p)*prsa[Pre][1])){
			dipr=p;break;
		}
	}
	if(p==-dipr)ifa++;
	if(ifa==2)printf("NO SOLUTION");
	else printf("%d",dipr);
	return 0;
}
