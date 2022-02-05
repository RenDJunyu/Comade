#include<stdio.h>
#include<stdbool.h>
int main(){
    int n;
    scanf("%d",&n);
    int object[n+1][2],//二维数组，0记录对象，1记录是否经过
        head[n+1],//记录告诉这个人的信息来源数目
        answer=n;
    bool node_sign=false;//是否存在分支
    for(int i=1;i<=n;i++)
        head[i]=0;
    for(int i=1;i<=n;i++){
        scanf("%d",&object[i][0]);
        object[i][1]=0;
        head[object[i][0]]++;
        if(head[object[i][0]]>1)node_sign=true;
        //如果某个人的信息来源超过1个，就存在分支
    }
    //去除分支
    while(node_sign){
        for(int i=1;i<=n;i++)
            if(head[i]==0){//从无信息来源者出发
                int next=i;
                while(head[next]<2){
                    //从起点到下一个分支汇点之间的人一定不属于圆
                    head[next]=-1;
                    next=object[next][0];
                }
                head[next]--;//到汇点后这个人失去一个信息来源
            }
        //检验是否还存在节点
        node_sign=false;
        for(int i=1;i<=n;i++)
            if(head[i]>1)
                node_sign=true;
    }
    //开始对剩下的圆处理
    for(int i=1;i<=n;i++)
        if(object[i][1]==0&&head[i]==1){
            //从没有被经过且属于圆任意的人开始
            int result=0;
            int check=i;
            do{
                result++;
                object[check][1]=1;
                check=object[check][0];
            }while(check!=i);
            answer=answer>result?result:answer;
        }
    printf("%d",answer);
    return 0;
}