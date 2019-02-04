#nithish
a,b=map(int,input().split())
for i in range(b,1000000):
	if(i%a==0 and i%b==0):
		print(i)
		break
	else:
		continue
