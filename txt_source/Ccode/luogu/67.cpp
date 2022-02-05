#include<stdio.h>
#include<math.h>
int main(){
	int n,m,k,x;
	scanf("%d %d %d %d",&n,&m,&k,&x);
	x=((long long)pow(10,k)*m%n+x)%n;
	printf("%d",x);
	return 0;
}
