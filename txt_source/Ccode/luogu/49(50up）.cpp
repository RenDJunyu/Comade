#include<stdio.h>
#include<math.h>
int change(int a,int b){
	int p=0,q=0;
	while(pow(10,p)<a)p++;
	while(pow(10,q)<b)q++;
	return a*pow(10,q)+b>b*pow(10,p)+a;
}
int main(){
	int n;
	scanf("%d",&n);
	int i,p,q,num[20];
	for(i=0;i<n;i++){
		scanf("%d",&num[i]);
	} 
	for(i=0;i<n;i++)
		for(p=i+1;p<n;p++)
			if(change(num[i],num[p])==0){
				q=num[i],num[i]=num[p],num[p]=q;
			}
	for(i=0;i<n;i++)printf("%d",num[i]);		
	return 0;		
} 
