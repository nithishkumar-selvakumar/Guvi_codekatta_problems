# your code goes here
#nithish
i=int(input())
n=input()
a=[]
b=[]
s=n.replace(" ","")
for n in s:
	if n not in a:
		a.append(n)
	else:
		b.append(n)
if b==[]:
	print("unique")
else:
	print(b[0])
		
	
