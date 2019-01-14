#nithish
n=int(input())
li=list(map(int,input().split(" ")))
li.sort()
a=((n+1)//2)
print(li[a-1])
