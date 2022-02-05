#include<stdio.h>
#include<math.h>
int ton(char word[100]){
	int p,time[26]={0},max,min;
	char i;
	for(p=0;p<=99;p++){
		if(word[p]==0)break; 
		time[word[p]-97]++;
	}
	max=0;min=100;
	for(p=1;p<=25;p++){
		max=max>time[p]?max:time[p];
		if(time[p]!=0)min=min<time[p]?min:time[p];
	}
	return max-min;
}
int judge(int n){
	if(n==2||n==3)return 1;
	else if(n==0||n==1)return 0;
	int i;
	for(i=2;i<=sqrt(n);i++){
		if(n%i==0)return 0;
	}
	if(i>sqrt(n))return 1;
}
int main(){
	char word[100]={'0'};
	gets(word);
	int i=ton(word);
	if(judge(i)==1){
		
		printf("Lucky Word\n%d",ton(word));
	}
	else {
		printf("No Answer\n0");
	}
	return 0;
} 
