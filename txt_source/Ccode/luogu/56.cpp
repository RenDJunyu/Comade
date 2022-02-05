#include<stdio.h>
int main(){
	int d,n,xy[129][129]={0};
	scanf("%d %d",&d,&n);
	int x,y,i=0,p,q,m,T=0,t,N=0;
	while(i<n){
		scanf("%d %d",&x,&y);
		scanf("%d",&xy[x][y]);
		i++;
	}
	for(i=0;i<129;i++)
		for(p=0;p<129;p++){
			for(t=0,q=-d;q<=d;q++)
				for(m=-d;m<=d;m++)
					if(i+q<129&&i+q>=0&&p+m<129&&p+m>=0)t+=xy[i+q][p+m];
			if(t>T){
				T=t;
				N=1;
			}
			else if(T==t)N++;
		}			
	printf("%d %d",N,T);
	return 0;
}
