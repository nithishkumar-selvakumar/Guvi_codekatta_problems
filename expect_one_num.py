# your code goes here
b=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
	d[i]=0
for i in a:
	d[i]=d[i]+1
for i,j in d.items():
	if j==1:
		print(i,end=" ")
