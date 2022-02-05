#include<stdio.h>
#include<stdlib.h>
typedef struct node{
    int loc;
    struct node *next;
}NODE;
NODE *get_stones(int L,int N);
void del_least_more(NODE *stone,int M,int left,int right);
int main(){
	int L,N,M;
	scanf("%d %d %d",&L,&N,&M);
    NODE *stones_list=get_stones(L,N);
    del_least_more(stones_list,M,1,L/(N-M+1));
	return 0;
}
NODE *get_stones(int L,int N){
    NODE *head=NULL,*tail,*p;
    for(int i=0;i<N+2;i++){
        p=(NODE *)malloc(sizeof(NODE));
        if(i==0)p->loc=0;
        else if(i==N+1)p->loc=L;
        else scanf("%d",&p->loc);
        p->next=NULL;
        if(head==NULL)head=p;
        else tail->next=p;
        tail=p;
    }
    return head;
}
void del_least_more(NODE *stone,int M,int left,int right){
    int last_m=0,out;
    while(left<=right){
        last_m=0;
        for(NODE *tmpnow=stone,*tmpnext=stone->next;tmpnext!=NULL;
            tmpnow=tmpnext,tmpnext=tmpnext->next)
            while(tmpnext->loc-tmpnow->loc<(left+right)/2){
                last_m++;
                tmpnext=tmpnext->next;
                if(tmpnext==NULL)break;
            }
        if(last_m>M)right=(left+right)/2-1;
        else {
            out=(left+right)/2;
            left=(right+left)/2+1;
        }
    }
    printf("%d",out);
}