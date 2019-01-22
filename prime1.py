#nithish
n=int(input())
i=2
while(i<n):
	a=n%i
	i=i+1
	if(a==0):
		break
if(i==n or n==2):
	print("yes")
else:
	print("no")
