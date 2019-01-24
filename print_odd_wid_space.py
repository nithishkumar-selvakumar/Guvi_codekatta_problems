# your code goes her
n=input()
ans=[]
for i in n:
	if(int(i)%2!=0):
		ans.append(i)
		if(i==len(ans)-1):
			print(i,end="")
		else:
			print(i,end="
