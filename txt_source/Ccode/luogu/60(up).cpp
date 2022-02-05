#include<stdio.h>
int main(){
	int n,form=0,mid=0,late,time=0,t=0;
	scanf("%d",&n);
	while(time++<n){
		scanf("%d",&late);
		if(form<mid&&mid>late)t+=mid;
		else if(form>mid&&mid<late)t-=mid;
		if(mid!=late)form=mid,mid=late;
	}
	if(form<mid)t+=mid;
	printf("%d",t);
	return 0; 
} 
