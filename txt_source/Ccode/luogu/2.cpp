#include<stdio.h>
int main()
{
	int a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a6,b6,a7,b7;
	scanf("%d %d %d %d %d %d %d %d %d %d %d %d %d %d",
	a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a6,b6,a7,b7);
	if(a1+b1>8)
	{printf("%d",1);
	}
	else if(a2+b2>8)
	{printf("%d",2);
	}
	else if(a3+b3>8)
	{printf("%d",3);
	}
	else if(a4+b4>8)
	{printf("%d",4);
	}
	else if(a5+b5>8)
	{printf("%d",5);
	}
	else if(a6+b6>8)
	{printf("%d",6);
	}
	else if(a7+b7>8)
	{printf("%d",7);
	}
	else 
	{printf("%d",0);	
	}
	return 0;
}
