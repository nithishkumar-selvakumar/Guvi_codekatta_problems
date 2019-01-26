#nithish
# your code goes here
m=int(input())
fact=1
if(m<0):
	print("no factorial")
elif(m==0):
	print("1")
else:
	for i in range(1,m+1):
		fact=fact*i
print(fact)	
