#nithish
n=input()
a=[]
for i in n.split():
	temp=i[::-1]
	a.append(temp)
print(*a)	
