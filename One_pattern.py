n=int(input())
if n!=2:
    for i in range(n,0,-1):
        for j in range(0,i):
            if i!=1:
                print("1",end=" ")
            else:
                print("1")
        if i!=1:
            print()
else:
    print("1 1")
    print("1")
