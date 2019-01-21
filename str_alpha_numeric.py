#nithishkumar
s=input()
a=0
n=0
for i in s:
	if i.isalpha():
		a+=1
	if i.isnumeric():
		n+=1
if a>0 and n>0:
	print("yes")
else:
	print("no")
