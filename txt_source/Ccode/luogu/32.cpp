#include<stdio.h>
int main()
{
	int M,N=0,f[10],n[100000]={0},t=0;
	scanf("%d",&M);
	for(f[0]=1;f[0]<=3;f[0]++)
	{
		for(f[1]=1;f[1]<=3;f[1]++)
		{
			for(f[2]=1;f[2]<=3;f[2]++)
			{
				for(f[3]=1;f[3]<=3;f[3]++)
				{
					for(f[4]=1;f[4]<=3;f[4]++)
					{
						for(f[5]=1;f[5]<=3;f[5]++)
						{
							for(f[6]=1;f[6]<=3;f[6]++)
							{
								for(f[7]=1;f[7]<=3;f[7]++)
								{
									for(f[8]=1;f[8]<=3;f[8]++)
									{
										for(f[9]=1;f[9]<=3;f[9]++)
										{
											if(f[0]+f[1]+f[2]+f[3]+f[4]+f[5]+f[6]+f[7]+f[8]+f[9]==M)
											{
												N++;
												n[t]=f[0],n[t+1]=f[1],n[t+2]=f[2],n[t+3]=f[3],n[t+4]=f[4],
												n[t+5]=f[5],n[t+6]=f[6],n[t+7]=f[7],n[t+8]=f[8],n[t+9]=f[9];
												t+=10;
											}
										}
										f[9]=0;
									}
									f[8]=0;
								}
								f[7]=0;
							}
							f[6]=0;
						}
						f[5]=0;
					}
					f[4]=0;
				}
				f[3]=0;
			}
			f[2]=0;
		}
		f[1]=0;
	}
	printf("%d\n",N);
	for(t=0;t<100000;t++)
	{
		if(n[t]==0)return 0;
		printf("%d ",n[t]);
		if(t%10==9)printf("\n");
	}
}
