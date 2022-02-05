#include<stdio.h>
#include<math.h>
int main(){
	long long size,loca;
	scanf("%lld %lld",&size,&loca);
	int i=0,p=size;
	while(i++<size){
		if(pow(2,p)>=loca&&loca>=pow(2,p-1)){
			printf("1");
			loca=(long long)pow(2,p--)-loca-1;
		}
		else{
			printf("0");
			p--;
		}
	}
	return 0;
}
