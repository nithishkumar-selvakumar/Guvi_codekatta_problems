#nithish
n=input()
li=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=[]
for i in range(len(n)):
	for j in range(len(li)):
		if(n[i]==li[j]):
			a.append(li[j+3])
for i in a:
    print(i.upper(),end="")


