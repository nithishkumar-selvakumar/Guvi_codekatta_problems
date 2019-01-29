#nithish
n=int(input())
l=list(map(int,input().split()))
d={}
a=[]
aa=[]
for i in l:
    d[i]=0
for i in l:
    d[i]=d[i]+1
for i,j in d.items():
    if j>1:
        a.append(i)
if len(a)==0:
    print("unique")
else:
    a.sort()
    print(*a)
