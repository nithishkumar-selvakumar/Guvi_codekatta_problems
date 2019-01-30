#hunter(3)
#nithish
n=int(input())
l=list(map(int,input().split(" ")))
a=[]
for i in range(len(l)):
    if(l[i]==i):
        a.append(i)
print(*a)        
