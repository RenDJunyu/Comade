#include<stdio.h>
#include<math.h>
int main(){
	int n;
	scanf("%d",&n);
	int i,p=0,q,a,t,max,num[21][2]={0},tem[20];
	for(i=0;i<n;i++){
		scanf("%d",&num[i][0]);
		num[i][1]=num[i][0];
		while(pow(10,p+1)<num[i][0])p++;
	}
	for(i=0;i<n;i++){
		while(num[i][1]<pow(10,p))num[i][1]*=10;
	}
	for(i=9;i>0;i--){
		for(t=0,a=0,q=0;q<n;q++){
			while(t<20)tem[t++]=0;
			if(num[q][1]>=i*pow(10,p)){
				tem[a]=q;a++;
			}
		}
		for(t=0;t<a;t++){
			for(max=21,q=0;q<a;q++){
				max=num[tem[q]][1]>num[max][1]?tem[q]:max;
			}
			if(max!=21){
				if(num[max][0]==32)printf("321");
				else if(num[max][0]==321)printf("32");
				else printf("%d",num[max][0]);
				num[max][0]=0;
				num[max][1]=0;
			}
		}	
	}
	return 0;
} 
