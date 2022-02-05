#include<stdio.h>
int main(){
	int n,i,a,b,size[10000][4]={0};
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d %d %d %d",&size[i][0],&size[i][1],
		&size[i][2],&size[i][3]);
	}
	scanf("%d %d",&a,&b);
	for(i=n-1;i>=0;i--){
		if(size[i][0]<=a&&a<=size[i][0]+size[i][2]&&
		size[i][1]<=b&&b<=size[i][1]+size[i][3]){
			printf("%d",i+1);return 0;
		}
	}
	if(i==-1)printf("-1");
	return 0;
}
