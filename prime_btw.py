#nithish kumar
def nithi(x):
	if x==0 or x==1:
		return False
	elif x==2:
		return True
	else:
		for i in range(2,x+1):
			if i==x:
				return True
			elif x%i==0:
				return False
a,b=map(int,input().split())
li=[]
for i in range(a+1,b):
	if nithi(i):
		li.append(i)
for i in range(len(li)):
	if i==len(li)-1:
		print(li[i],end="")
	else:
		print(li[i],end=" ")
