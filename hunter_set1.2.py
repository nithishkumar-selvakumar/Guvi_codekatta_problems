#nithish
n=int(input())
l=list(map(str,input().split(" ")))
l.sort(reverse=True)
print("".join(l))
