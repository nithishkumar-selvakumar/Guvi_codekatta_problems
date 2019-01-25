# your code goes h
#nithish
n=input()
li=[]
l=[]
a=n[0::2]
b=n[1::2]
li.append(a)
l.append(b)
print(''.join(map(str,li)),end=" ")
print(''.join(map(str,l)))
