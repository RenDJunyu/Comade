#include<stdio.h>
int main(){
	int p1,p2,p3;
	char sen[101]={0};
	scanf("%d %d %d\n",&p1,&p2,&p3);
	gets(sen);
	int i;
	for(printf("%c",sen[0]),i=1;sen[i]>0;i++){
		if(sen[i]=='-'&&sen[i+1]!=0)
			if(sen[i-1]>sen[i+1]||sen[i-1]==sen[i+1]||(sen[i-1]-58)*(sen[i+1]-58)<0||sen[i-1]=='-')printf("-");
			else if(p3==1)for(char c=sen[i-1]+1;c<=sen[i+1]-1;c++)
				if(p1==1||p1==2)
					for(int p=0;p<p2;p++)
						printf("%c",c-32*(p1-1)*(c>58));
				else for(int p=0;p<p2;p++)
					printf("*");
			else for(char c=sen[i+1]-1;c>=sen[i-1]+1;c--)
				if(p1==1||p1==2)
					for(int p=0;p<p2;p++)
						printf("%c",c-32*(p1-1)*(c>58));
				else for(int p=0;p<p2;p++)
					printf("*");
		else printf("%c",sen[i]);
	}
	return 0;
}
