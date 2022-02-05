#include<stdio.h>
#include<string.h>
int combine(char *p1,char*p2){
	int a=strlen(p1),b=strlen(p2);
	for(int i=1,p;i<a&&i<b;i++){
		for(p=0;p<i;p++)
			if(p1[a+p-i]!=p2[p])break;
		if(p==i){
			for(int r=0;r+p<b;r++)
				p1[a+r]=p2[p+r];
			return 1;
		}
	}
	return 0;
}
int compare(char *p1,char*p2){
	int a=strlen(p1),b=strlen(p2);
	for(int i=1,p;i<a&&i<b;i++){
		for(p=0;p<i;p++)
			if(p1[a+p-i]!=p2[p])break;
		if(p==i)return 1;
	}
	return 0;
}
int main(){
	int n;
	scanf("%d\n",&n);
	char words[n+1][1000]={0},start;
	int i,p,r=0,q,a,m,csort[4][n+1]={0},mlen=0,add=0;
	int record[2*n]={0};
	for(i=0;i<n;i++){
		gets(words[i]);
		mlen=mlen<strlen(words[i])?strlen(words[i]):mlen;
		if(compare(words[i],words[i]))
			csort[0][r++]=i;
	}
	csort[0][n]=r;
	for(r=0,i=0;i<n;i++)
		for(p=0;p<n;p++)
			if(compare(words[i],words[p])&&compare(words[p],words[i])){
				csort[1][r++]=i;
				break; 
			}
	csort[1][n]=r;
	for(r=0,i=0;i<n;i++)
		for(p=0;p<n;p++)
			if(compare(words[i],words[p])){
				csort[2][r++]=i;
				break; 
			}
	csort[2][n]=r;
	for(q=0,r=0;q<3;q++){
		for(i=mlen;i>0;i--)
			for(p=0;p<csort[q][n];p++){
				if(words[csort[q][p]][999]==2)continue;
				if(strlen(words[csort[q][p]])==i){
					csort[3][r++]=csort[q][p];
					words[csort[q][p]][999]=2;
				}
			}	
	}
	for(i=mlen;i>0;i--)
		for(p=0;p<n;p++){
			if(words[p][999]==2)continue;
			if(strlen(words[p])==i){
				csort[3][r++]=p;
				words[p][999]=2;
			}
		}	
	scanf("%c",&start);
	for(i=0,q=0;i<n;i++){
		if(words[csort[3][i]][0]!=start)continue;
		csort[3][n]=n;
		record[q++]=csort[3][n];
		strcpy(words[n],words[csort[3][i]]);
		words[n][999]=1;
		for(p=0;p<2*n;p++){
			for(r=0;r<n;r++){
				if(r==i)r=n;
				if(words[csort[3][r]][999]==3){
					if(r==n)r=i;
					continue;
				}
				if(combine(words[csort[3][i]],words[csort[3][r]])){
					if(words[csort[3][r]][999]!=1)words[csort[3][r]][999]=1;
					else words[csort[3][r]][999]=3;
					record[q++]=csort[3][r];
					break;
				}
				if(r==n)r=i;
			}
			if(r>n)break;
		}
		for(m=0,a=-1,p=0;m<=n;m++){
			if(words[m][999]==3||compare(words[record[q-2]],words[m])!=1||m==csort[3][i])continue;
			p=strlen(words[m])-strlen(words[record[q-1]]);
			if(add<p){
				add=p;
				a=m;
			}
		}
		if(a>-1)
			for(r=0;r<=n;r++){
				if(words[r][999]==3||strlen(words[r])>mlen)continue;
				p=strlen(words[a]);
				if(combine(words[a],words[r]))
					p=strlen(words[a])-p;
			}	
		add+=strlen(words[csort[3][i]])+p;	
		printf("%d",add);
		return 0;	
	}
}
