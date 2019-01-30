#nithish hunter
n=int(input())
a=[]
l=list(map(int,input().split()))
for i in range(n):
    if l[i] in l[i+1:]:
        a.append(l[i])
a=set(a)
l=set(l)
d=l.difference(a)
print(*d)
