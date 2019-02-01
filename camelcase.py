# your code goes here
s=input()
l=list(map(str,s.split()))
ans=""
for i in l:
	ans+=i.capitalize()
	ans+=" "
print(ans)
