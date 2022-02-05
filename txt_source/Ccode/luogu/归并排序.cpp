#include<stdio.h>
int Msort(int *num,int s,int e){
	if(s<e){
		int m=(s+e)/2;
		Msort(num,s,m);
		Msort(num,m+1,e);
    	int L[m-s+1], R[e-m]; 
    	for(int i=s;i<=e;i++){
    		if(i<=m)L[i-s]=num[i];
    		else R[i-m-1]=num[i];
		}
    	int s1=0,s2=0,i=s;
    	while(s1<m-s+1&&s2< e-m){
    	    num[i++]=L[s1]<R[s2]?L[s1++]:R[s2++];
    	}	
    	while(s1 < m-s+1){
    	    num[i++]=L[s1++];
    	}
	}
}
int main(){
	int num[11]={-1,2,4,-12,4,0,0,12,23,-4,7000};
	Msort(num,0,10);
	for(int i=0;i<11;i++)printf("%d ",num[i]);
	return 0;
}
//三线归并
/*#include<stdio.h>
int Msort(int *num,int s,int e){
	if(s<e){
		int m1=s+(e-s)/3,m2=s+2*(e-s)/3;
		Msort(num,s,m1);
		Msort(num,m1+1,m2);
		Msort(num,m2+1,e);
    	int L[m1-s+1],M[m2-m1],R[e-m2]; 
    	for(int i=s;i<=e;i++)
    		if(i<=m1)L[i-s]=num[i];
    		else if(i>m1&&i<=m2)M[i-m1-1]=num[i];
			else R[i-m2-1]=num[i];
    	int s1=0,s2=0,s3=0,i=s;
    	while(s1<m1-s+1&&s2<m2-m1&&s3<e-m2)
            if(L[s1]<M[s2]&&L[s1]<R[s3])num[i++]=L[s1++];
            else if(M[s2]<L[s1]&&M[s2]<R[s3])num[i++]=M[s2++];
            else if(R[s3]<M[s2]&&R[s3]<L[s1])num[i++]=R[s3++];
    	while(s1<m1-s+1&&s2<m2-m1)
    	    num[i++]=L[s1]<M[s2]?L[s1++]:M[s2++];
        while(s1<m1-s+1&&s3<e-m2)
    	    num[i++]=L[s1]<R[s3]?L[s1++]:R[s3++];
        while(s2<m2-m1&&s3<e-m2)
    	    num[i++]=M[s2]<R[s3]?M[s2++]:R[s3++];
        while(s1<m1-s+1)num[i++]=L[s1++];
        while(s2<m2-m1)num[i++]=M[s2++];
        while(s3<e-m2)num[i++]=R[s3++];
	}
}
int main(){
    int n;
    scanf("%d",&n);
	int num[n];
    for(int i=0;i<n;i++)
        scanf("%d",&num[i]);
	Msort(num,0,n-1);
	for(int i=0;i<n;i++)printf("%d ",num[i]);
	return 0;
}*/