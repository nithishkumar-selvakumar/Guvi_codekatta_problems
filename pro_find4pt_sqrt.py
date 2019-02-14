# your code goes here
#nithish
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
a=y2-y1
b=y3-y4
c=x3-x2
d=x4-x1
if a==b and c==d:
	print("yes")
else:
	print("no")
