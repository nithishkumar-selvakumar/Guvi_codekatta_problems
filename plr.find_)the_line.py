# your code goes here
#nithish
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
if(a==e==c):
	print("yes")
elif(b==d==f):
	print("yes")
elif(a==b and c==d and e==f):
	print("yes")
else:
	print("no")
