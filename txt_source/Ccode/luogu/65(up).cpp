#include<stdio.h>
#include<string.h>
int compare(char *p1,char*p2){
	int a=strlen(p1),b=strlen(p2);
	for(int i=1,p;i<a&&i<b;i++){
		for(p=0;p<i;p++)
			if(p1[a+p-i]!=p2[p])break;
		if(p==i)return a+b-i;
	}
	return 0;
}
int n,len;
int search(int form,int lenth,char words[20][100]){
	words[form][99]++;
	int i,p;
	for(i=0;i<n;i++)
		if(words[form][99]!=2&&(p=compare(words[form],words[i]))){
			lenth+=p;
			search(i,lenth,words);
		}
	if(i==n&&len<lenth)len=lenth;
}
int main(){
	scanf("%d\n",&n);
	char start,words[20][100]={0};
	int i,p,q,len=0;
	for(i=0;i<n;i++)gets(words[i]);
	scanf("%c",&start);
	for(i=0;i<n;i++)
		if(words[i][0]==start){
			len=strlen(words[i]);
			search(i,len,words);
		}
	printf("%d",len);
	return 0;
}
