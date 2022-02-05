#include<stdio.h>
int main(){
	int M,D,t=0;
	scanf("%d-%d",&M,&D);
	if(M>12||M<1)t++;
	if(M==2&&D>28)t++;
	if(D>31||D<1)t++;
	printf("%d",t);
	return 0;
}
