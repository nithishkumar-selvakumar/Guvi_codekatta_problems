#nithish
n=int(input())
s=input()
ans=""
l=['a','e','i','o','u']
for i in s:
	if i in l:
		continue
	else:
		ans=ans+i
print(ans[::-1])		
