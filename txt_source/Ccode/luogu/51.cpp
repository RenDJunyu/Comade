#include<stdio.h>
int NUM[200000];
int Msort(int *NUM,int s,int e){
	if(s<e){
		int m=(s+e)/2;
		Msort(NUM,s,m);
		Msort(NUM,m+1,e);
    	int L[m-s+1],R[e-m]; 
    	for(int i=s;i<=e;i++){
    		if(i<=m)L[i-s]=NUM[i];
    		else R[i-m-1]=NUM[i];
		}
    	int s1=0,s2=0,i=s;
    	while(s1<m-s+1&&s2<e-m){
    	    NUM[i++]=L[s1]<R[s2]?L[s1++]:R[s2++];
    	}	
    	while(s1<m-s+1){
    	    NUM[i++]=L[s1++];
    	}
	}
}
int main(){
	int n;
	scanf("%d",&n);
	int i,p,num;
	for(i=0;i<n;i++){
		scanf("%d",&NUM[i]);
	}
	Msort(NUM,0,n-1);
	for(i=0;i<n;i++){
		num=NUM[i];
		p=1;
		while(NUM[i+1]==num&&i<n){
			p++;i++;
		}
		printf("%d %d",num,p);
		if(i<n)printf("\n");
	}
	return 0;
} 
