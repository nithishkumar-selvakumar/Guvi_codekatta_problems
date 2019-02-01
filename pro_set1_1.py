n=int(input())
s=[]
for i in range(n):
    s.append([])
#print(s)
for i in range(n):
    t=input()
    s[i].append(t)
#print(s)
#for i in range(len(s)):
#    print(i,s[i])
minimum=len(s[0][0])
for i in range(n):
    if len(s[i][0])<minimum:
        minimum=len(s[i][0])
#print(minimum)
ans=""
for i in range(minimum):
    condition=True
    for j in range(n-1):
        #print(j)
        if s[j][0][i]!=s[j+1][0][i]:
            condition=False
            break
    if condition:
        ans+=s[n-1][0][i]
    else:
        break
print(ans)
