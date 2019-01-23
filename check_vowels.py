#nithiush
n=input()
c=0
for i in n:
	if i in ('a','e','i','o','u'):
		c=c+1
		if(c>0):
			print("yes")
		else:
			print("no")
