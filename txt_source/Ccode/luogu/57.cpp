#include<stdio.h>
int main(){
	char acc[101]={'0'};
	gets(acc);
	char put;
	int i=0;
	while(1){
		put=getchar();
		if(put=='\n')break;
		if(acc[i]>90)acc[i]-=32;
		if(put>64&&put<91){
			if(put>=acc[i])printf("%c",put+65-acc[i]);
			else printf("%c",put+91-acc[i]);
		}
		else if(put>96){
			if(put-32>=acc[i])printf("%c",put+65-acc[i]);
			else printf("%c",put+91-acc[i]);
		}
		if(acc[++i]==0)i=0;
	}
	return 0;
}
