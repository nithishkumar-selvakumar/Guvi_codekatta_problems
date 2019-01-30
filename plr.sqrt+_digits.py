#noithish
n=int(input())
s=0
z=0
while n>0:
	b=n%10
	z=b*b+z
	n=n//10
print(z)	
