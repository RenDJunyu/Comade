#include<stdio.h>
int main()
{
	float X=0,N=0;
	int c=0,i;
	char fc[100]="0",a;
	scanf("%s",fc);
	for(i=0;i<=99;i++){
		if(fc[i]=='=')break;
		if(i==0&&fc[i]>=48||fc[i]=='+'){
			if(fc[i]>=97){
				a=fc[i];X+=1;continue;
			}
			if(fc[i]>=48&&fc[i]<=59){
				while(fc[i]>=48&&fc[i]<=57&&fc[i]!='='){
					c=c*10+fc[i]-48;i++;
				}
				if(fc[i]>=97){
					a=fc[i];X+=c;c=0;continue;
				}
				if(fc[i]<=45||fc[i]=='='){
					N-=c;c=0;
					if(fc[i]=='=')break;
					i--;continue;
				}
			}
			else if(fc[i]=='+'){
				i++;
				if(fc[i]>=97){
					a=fc[i];X+=1;continue;
				}
				if(fc[i]>=48&&fc[i]<=59){
					while(fc[i]>=48&&fc[i]<=57&&fc[i]!='='){
						c=c*10+fc[i]-48;i++;
					}
					if(fc[i]>=97){
						a=fc[i];X+=c;c=0;continue;
					}
					if(fc[i]<=45||fc[i]=='='){
						N-=c;c=0;
						if(fc[i]=='=')break;
						i--;continue;
					}
				}
			}	
		}
		else if(fc[i]=='-'){
			i++;
			if(fc[i]>=97){
				a=fc[i];X-=1;continue;
			}
			if(fc[i]>=48&&fc[i]<=59){
				while(fc[i]>=48&&fc[i]<=57&&fc[i]!='='){
					c=c*10+fc[i]-48;i++;
				}
				if(fc[i]>=97){
					a=fc[i];X-=c;c=0;continue;
				}
				if(fc[i]<=45||fc[i]=='='){
					N+=c;c=0;
					if(fc[i]=='=')break;
					i--;continue;
				}
			}
		}
	}
	int I=i+1;
	for(i++;i<=99;i++){
		if(fc[i]==48)break;
		if(i==I&&fc[i]>=48||fc[i]=='+'){
			if(fc[i]>=97){
				a=fc[i];X-=1;continue;
			}
			if(fc[i]>=48&&fc[i]<=59){
				while(fc[i]>=48&&fc[i]<=57&&fc[i]!=48){
					c=c*10+fc[i]-48;i++;
				}
				if(fc[i]>=97){
					a=fc[i];X-=c;c=0;continue;
				}
				if(fc[i]<=45||fc[i]==0){
					N+=c;c=0;
					if(fc[i]==0)break;
					i--;continue;
				}
			}
			else if(fc[i]=='+'){
				i++;
				if(fc[i]>=97){
					a=fc[i];X-=1;continue;
				}
				if(fc[i]>=48&&fc[i]<=59){
					while(fc[i]>=48&&fc[i]<=57&&fc[i]!=0){
						c=c*10+fc[i]-48;i++;
					}
					if(fc[i]>=97){
						a=fc[i];X-=c;c=0;continue;
					}
					if(fc[i]<=45||fc[i]==48){
						N+=c;c=0;
						if(fc[i]==48)break;
						i--;continue;
					}
				}
			}	
		}
		else if(fc[i]=='-'){
			i++;
			if(fc[i]>=97){
				a=fc[i];X-=1;continue;
			}
			if(fc[i]>=48&&fc[i]<=59){
				while(fc[i]>=48&&fc[i]<=59&&fc[i]!=48){
					c=c*10+fc[i]-48;i++;
				}
				if(fc[i]>=97){
					a=fc[i];X+=c;c=0;continue;
				}
				if(fc[i]<=45||fc[i]==48){
					N-=c;c=0;
					if(fc[i]==48)break;
					i--;continue;
				}
			}
		}
	}
	if(N==0)X=1;
	printf("%c=%.3f",a,N/X);
	return 0;
}
