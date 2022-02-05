#include<stdio.h>
int money(int endgra,int clagra,char orboss,char orwest,int essay){
	int sum=0;
	if(endgra>80&&essay>=1)sum+=8000;
	if(endgra>85&&clagra>80)sum+=4000;
	if(endgra>90)sum+=2000;
	if(endgra>85&&orwest=='Y')sum+=1000;
	if(clagra>80&&orboss=='Y')sum+=850;
	return sum;
}
int main(){
	int N,endgra[100]={0},clagra[100]={0},essay[100]={0};
	char name[100][20]={'0'},orboss[100]={'0'},orwest[100]={'0'};
	scanf("%d",&N);
	int i,p,q,sum=0,last,top=0;
	for(i=0;i<N;i++){
		scanf("%s",&name[i]);
		scanf("%d %d %c %c %d",&endgra[i],&clagra[i],&orboss[i],&orwest[i],&essay[i]);
		last=money(endgra[i],clagra[i],orboss[i],orwest[i],essay[i]);
		if(last>top){
			top=last;p=i;
		}
		sum+=last;
	}
	for(i=0;name[p][i]!=0;i++){
		printf("%c",name[p][i]); 
	}
	printf("\n%d\n%d",top,sum);
}
