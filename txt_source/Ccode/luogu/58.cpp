#include<stdio.h>
int main(){
	int N,start,stan,i,p;
	scanf("%d",&N);
	start=N/2*(N+2)-2*N;
	for(i=0;i<N;i++){
		if(i<N-1)start=(start+N+1)%(N*N);
		else if(i==N-1)start=(start+1)%(N*N);
		for(p=0,stan=start;p<N;p++){
			if(i==N-1&&p==0)stan=(stan+N+2)%(N*N);
			else if(p==N/2-i/2||p==N-(i+1)/2)stan=(stan+2)%(N*N);
			else stan=(stan+N+2)%(N*N);
			printf("%d",stan+(stan==0)*(N*N));
			if(p<N-1)printf(" ");
			else if(i<N-1)printf("\n");
		}
	}
	return 0;
}
