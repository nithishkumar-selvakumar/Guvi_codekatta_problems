# your code goes here
n=int(input())
sum=0
while(n>0):
	temp = n%10
	sum=sum+temp
	n=n//10
print(sum)	
