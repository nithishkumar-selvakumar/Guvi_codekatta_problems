#nithish
n,k=map(int,input().split())
s=list(map(int,input().split()))
q=sorted(s,reverse=True)
print(q[k-1])
