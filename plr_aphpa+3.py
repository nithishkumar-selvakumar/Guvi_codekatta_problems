#nithish
n=input()
li=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=[]
for i in range(len(n)):
	for j in range(len(li)):
		if(n[i]==li[j]):
			a.append(li[j+3])
for i in a:
    print(i.upper(),end="")

