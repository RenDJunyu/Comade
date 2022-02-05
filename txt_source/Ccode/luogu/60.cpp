#include<stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	int hei[n+1]={0};
	hei[n]=-1;
	int i=0,t=0,start=0,end;
	while(i<n)scanf("%d",&hei[i++]);
	while(start<n){
		start--;
		while(hei[++start]==0);
		end=start-1;
		while(hei[++end]>0)hei[end]--;
		t++;
	}
	printf("%d",--t);
	return 0; 
} 
