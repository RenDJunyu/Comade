#include<stdio.h>
int main(){
	int max,a;
	scanf("%d",&max);
	for(int i=0;i<=max;i++){
		scanf("%d",&a);
		if(i==0){
			if(a>0){
				if(a==1){
					printf("x^%d",max-i);
					continue;
				}
				printf("%dx^%d",a,max-i);
			}
			if(a<0){
				if(a==-1){
					printf("-x^%d",max-i);
					continue;
				}
				printf("%dx^%d",a,max-i);
			}
		}
		else if(i==max){
			if(a>0)printf("+%d",a);
			if(a<0)printf("%d",a);
			return 0;
		}
		else if(i==max-1){
			if(a>0){
				if(a==1){
					printf("+x");
					continue;
				}
				printf("+%dx",a);
			}
			if(a<0){
				if(a==-1){
					printf("-x");
					continue;
				}
				printf("%dx",a);
			}			
		}
		else{
			if(a>0){
				if(a==1){
					printf("+x^%d",max-i);
					continue;
				}
				printf("+%dx^%d",a,max-i);
			}
			if(a<0){
				if(a==-1){
					printf("-x^%d",max-i);
					continue;
				}
				printf("%dx^%d",a,max-i);
			}				
		}	
	}
}
