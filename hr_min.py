# your code goes here
n=int(input())
if n<60:
	d=n%60
	print('0',d)
else:
	s=n//60
	p=n%60
	print(s,p)
