#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
    char *newcode=NULL,letter;
    int order=0;
    while((letter=getchar())!='\n'){
        newcode=(char *)realloc(newcode,sizeof(char)*(order+1));
        newcode[order++]=letter;
    }
    char oldcode[order];
    gets(oldcode);
    char codebook[26]={0};
    for(int i='A';i<='Z';i++){
        for(int j=0;j<order;j++){
            if(oldcode[j]==i){
                if(codebook[i-'A']==0)
                    codebook[i-'A']=newcode[j];
                else if(codebook[i-'A']!=newcode[j]){
                    printf("Failed");
                    return 0;
                }
            }
        }
        if(codebook[i-'A']==0){
            printf("Failed");
            return 0;
        }
    }
    while((letter=getchar())!='\n')
        for(int i=0;i<26;i++){
            if(codebook[i]==letter)
            printf("%c",i+'A');
        }
    return 0;
}