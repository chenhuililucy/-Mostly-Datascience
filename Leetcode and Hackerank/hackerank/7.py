import math

N = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]
mean=sum(arr)/N
n=0
for no in arr:
    n=n+(no-mean)**2
#print(n)
ans=math.sqrt(n/N)
print('{:.1f}'.format(ans))