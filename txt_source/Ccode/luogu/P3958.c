#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<math.h>
#define distance(A,B) (sqrt(pow(A->x-B->x,2)+pow(A->y-B->y,2)+pow(A->z-B->z,2))<=2*r)
typedef struct node{
    int x,y,z;
    bool passed;
    struct node *next;
}NODE;
void get_A_find();
NODE *get_list(int n);
int find_way(int h,int r,NODE *head,NODE *kont);
void free_list(NODE *head);
int main(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        if(i>0)putchar('\n');
        get_A_find();
    }
}
void get_A_find(){
    int n,h,r;
    scanf("%d %d %d",&n,&h,&r);
    NODE *head=get_list(n);
    if(find_way(h,r,head,NULL))
        printf("Yes");
    else printf("No");
}
NODE *get_list(int n){
    NODE *head=NULL,*tail,*p;
    for(int i=0;i<n;i++){
        p=(NODE *)malloc(sizeof(NODE));
        scanf("%d %d %d",&p->x,&p->y,&p->z);
        p->passed=false;
        p->next=NULL;
        if(head==NULL)head=p;
        else tail->next=p;
        tail=p;
    }
    return head;
}
int find_way(int h,int r,NODE *head,NODE *knot){
    bool result=false;
    if(knot==NULL){
        NODE *tmp=head;
        while(tmp!=NULL){
            if(tmp->z<=r){
                tmp->passed=true;
                result|=find_way(h,r,head,tmp);
            }
            tmp=tmp->next;
        }
    }
    else {
        if(knot->z+r>=h)result|=true;
        else {
            NODE *tmp=head;
            while(tmp!=NULL){
                if(!tmp->passed&&distance(tmp,knot)){
                    tmp->passed=true;
                    result|=find_way(h,r,head,tmp);
                }
                tmp=tmp->next;
            }
        }
    }
    return result;
}
void free_list(NODE *head){
    NODE *tmp=head;
    while(head!=NULL){
        tmp=tmp->next;
        free(head);
        head=tmp;
    }
}