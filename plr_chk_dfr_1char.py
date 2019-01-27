#nithish
a,b=map(str,input().split())
c=0
aa=list(a)
bb=list(b)
aa.sort()
bb.sort()
for i in range(len(aa)):
	if aa[i]==bb[i]:
		c+=1
	else:
		break
print("yes" if len(a)-1==c else "no")
