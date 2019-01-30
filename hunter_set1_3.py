#nithish
#hunter
n=int(input())
l=list(map(int,input().split(" ")))
a=[]
for i in range(len(l)):
    if(l[i]==i):
        a.append(i)
if len(a)>0:
    print(*a)
else:
    print(-1)
