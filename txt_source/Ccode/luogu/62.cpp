#include<stdio.h>
#include<math.h>
double A,B,C,D;
double func(double x){
	return A*pow(x,3)+B*pow(x,2)+C*x+D;
}
int main(){
	int i,p;
	double Xn[3][2]={0};
	scanf("%lf %lf %lf %lf",&A,&B,&C,&D);
	for(i=-100,p=0;i<101&&p<3;i++)
		if(func(i)*func(i+1)<0)Xn[p][0]=i,Xn[p][1]=1,p++;
		else if(func(i)==0)Xn[p][0]=i,Xn[p][1]=3,p++;
	for(i=0;i<3;i++)
		for(p=0;p<3;p++){
			if(Xn[i][1]==4)break;
			while(1){
				if(func(Xn[i][0]+pow(0.1,Xn[i][1]))*func(Xn[i][0])<0)break;
				else if(func(Xn[i][0])==0){
					Xn[i][1]=3;
					break;
				}
				Xn[i][0]+=pow(0.1,Xn[i][1]);
			}
			Xn[i][1]++;
		}
	printf("%.2lf %.2lf %.2lf",Xn[0][0],Xn[1][0],Xn[2][0]);
	return 0;
} 
