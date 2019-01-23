#nithish
n=int(input())
a,b=map(int,input().split())
c=0
for i in range(a,b+1):
	if i==n:
		c=c+1
if(c>0):
	print("yes")
else:
	print("no")
		
