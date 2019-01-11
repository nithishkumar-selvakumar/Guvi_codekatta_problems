a,k=input().split()
a=int(a)
k=int(k)
arr=[]
c=0
for i in range(0,a):
  arr.append(int(input()))
print(sum(arr[0:k]))
