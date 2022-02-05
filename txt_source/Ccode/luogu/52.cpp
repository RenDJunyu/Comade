#include<stdio.h>
int main(){
	int N;
	scanf("%d",&N);
	int num[N],i=0,aver=0,t=0;
	while(i<N){
		scanf("%d",&num[i]);
		aver+=num[i];
		i++;
	}
	aver/=N;
	for(i=0;i<N/2;i++){
		if(num[i]<aver)num[i+1]-=aver-num[i],t++;
		else if(num[i]>aver)num[i+1]+=num[i]-aver,t++;
		if(num[N-i-1]<aver)num[N-i-2]-=aver-num[N-i-1],t++;
		else if(num[N-i-1]>aver)num[N-i-2]+=num[N-i-1]-aver,t++;
	}
	printf("%d",t);
	return 0;
}
