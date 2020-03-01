def median(a, l, r): 
    n = r - l + 1
    n = (n + 1) // 2 - 1
    return n + l 
  
# Function to calculate IQR 
def IQR(a, n): 
  
    a.sort() 
  
    Q1 = a[median(a, 0, mid_index)] 

    # Index of median of entire data 
    mid_index = median(a, 0, n) 
  
    # Median of first half 
  
    # Median of second half 
    Q3 = a[median(a, mid_index + 1, n)] 



import numpy
N=input() 
a = numpy.array(input())
print(numpy.percentile(a, 25))
print(numpy.percentile(a, 50))
print(numpy.percentile(a, 75))

