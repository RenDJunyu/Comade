#include<stdio.h>
int main(){
	int n,m,k;
	scanf("%d %d %d",&n,&m,&k);
	int PTD[1000][1000]={0},TD[1000][1000]={0},DT[1000]={0},i,p;
	for(i=0;i<n;i++){
		for(p=0;p<m;p++)
		scanf("%d",&PTD[i][p]);
		if(TD[p][PTD[i][p]-1]==0)TD[p][PTD[i][p]-1]++;
	}
	for(p=0;p<k;p++){ 
		for(i=0;i<k;i++){
			if(TD[i][p]==1)DT[p]++; 
		}
		printf("%d ",DT[p]);
	}
	return 0;
}
