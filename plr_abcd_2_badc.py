#nithish
n=input()
ans=""
for i in range(0,len(n)-1,2):
	ans=ans+n[i+1]
	ans=ans+n[i]
print(ans)
