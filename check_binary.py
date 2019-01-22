#nithish
n=input()
count=0
for i in range(0,len(n)):
	if n[i]!='1' and n[i]!='0':
		count=count+1
if count==0:
	print("yes")
else:
	print("no")
