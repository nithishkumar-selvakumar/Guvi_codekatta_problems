#int
def nithi(n):
	on=n
	s=0
	while n>0:
		d=n%10
		s=s+(d**3)
		n=n//10
	if s==on:
		return True
	else:
		return False
n,a=map(int,input().split())
a1=[]
for i in range(n+1,a):
	if nithi(i):
		a1.append(i)
for i in range(len(a1)):
	if i==len(a1)-1:
		print(a1[i],end="")
	else:
		print(a1[i],end=" ")
		
		
