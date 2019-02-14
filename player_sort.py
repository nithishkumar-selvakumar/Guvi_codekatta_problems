# your code goes here
#nithish
n=int(input())
a=[]
for i in range(n):
	t1=list(map(int,input().split()))
	a.extend(t1)
a.sort()
print(*a)
