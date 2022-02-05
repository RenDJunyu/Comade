p,k=input().split()
p,k=int(p),int(k)
sentence=""
for i in range(p):
    sentence=sentence+'/'+input()
usage=[0 for i in range(len(sentence))]
s=int(input())
dictionary=[]
total=0
for i in range(s):
    dictionary.append(input())
for i in dictionary:
    start=0
    flag=False
    for j in dictionary:
        if j!=i and j.find(i)==0:
            flag=True
            break
    if flag:continue
    while 1:
        loc=sentence.find(i,start)
        start=loc+1
        if loc==-1:
            break
        total+=1
        for j in range(loc,loc+len(i)):
            usage[j]+=1
k=0 if usage.count(0)>=k else k-usage.count(0)
print(total-k)