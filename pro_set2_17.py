#nithiush pro
a,b=map(int,input().split(" "))
s=0
li=list(map(int,input().split(" ")))
for i in range(len(li)):
	for j in range(i+1,len(li)):
		if(li[i]+li[j]==b):
			s=1
		else:
			continue
if s>0:
	print("yes")
else:
	print("no")
