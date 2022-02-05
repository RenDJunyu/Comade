int Qsort(int *num, int left, int right){
    if(left>=right)return 0;
    int i=left;
    int p=right;
    int key=num[left];
    while(i<p){
        while(i<p&&key<=num[p])p--;
        num[i]=num[p]; 
        while(i<p&&key>=num[i])i++;
        num[p]=num[i];
    }
    num[i]=key;
    Qsort(num,left,i-1);
    Qsort(num,i+1,right);             
}