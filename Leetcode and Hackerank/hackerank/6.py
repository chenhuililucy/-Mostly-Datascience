
from itertools import repeat


def median(c, l, r): 
    n = r - l + 1
    n = (n + 1) // 2 - 1
    return n + l 

def IQR(c, n): 
  
    c.sort() 
  
    Q1 = c[median(c, 0, mid_index)] 

    # Index of median of entire data 
    mid_index = median(c, 0, n) 
  
    # Median of first half 
  
    # Median of second half 
    Q3 = c[median(c, mid_index + 1, n)] 

import numpy
N = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
b = [int(i) for i in input().strip().split(' ')]
c=[]


for i in range(N):
    for j in range(b[i]):
        c.append(a[i])

print(c)

low=numpy.percentile(c, 25)
print(low)
mid=numpy.percentile(c, 50)
up=numpy.percentile(c, 75)
print(up)
print(up-low)

