#nithish
n=int(input())
c=0
li=list(map(int,input().split()))
for i in li:
	c=li.index(i)
	print(i,end=" ")
	print(c)
