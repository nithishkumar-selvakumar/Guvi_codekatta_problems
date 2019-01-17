#nithish.s
num=int(input())
temp = 0
first = 0
second = 1
count = 1
print(second,end=" ")
while count < num:
	temp = first + second
	first = second
	count = count + 1
	if count == num:
		print(temp,end="")
	else:
		print(temp,end=" ")
