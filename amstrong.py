# your code goes here
a=int(input())
c=str(a)
d=len(c)
temp=0
temp1=a
while a>0:
	n=a%10
	f=n**d
	temp=temp+f
	n=n//10
if temp1==temp:
	print("yes")
else:
	print("no")
