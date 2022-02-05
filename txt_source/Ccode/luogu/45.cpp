#include<stdio.h>
char dj[100000][12]={'0'};
int dn[100000][2]={0};
int main(){
	int n,m,i,p;	
	scanf("%d %d\n",&n,&m);
	for(i=0;i<n;i++){
		p=0;
		for(;p<13;p++){
			scanf("%c",&dj[i][p]);
			if(dj[i][p]=='\n'&&p!=0){
				dj[i][p]=0;
				break;
			} 
		}
	}
	for(i=0;i<m;i++){
		scanf("%d %d",&dn[i][0],&dn[i][1]);
	}
	for(i=0,p=0;p<m;p++){
		if((((dj[i][0]=='1')*10+dn[p][0])%11)!=0)
			i+=dn[p][1]%n;
		else i+=n-dn[p][1]%n;
		i%=n;
	}
	for(p=2;p<12;p++){
		if(dj[i][p]==0)break;
		printf("%c",dj[i][p]);
	}
	return 0;
}
