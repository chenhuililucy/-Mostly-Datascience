
""" 
Learning collections: high-performing container data 
1.1 Counter objects 
count=counter()
for word in ['hello','goodbye']
    count[word]+=1 
print(count)

def(wordcounter): 
    words=re.findall(r'\w+',open('hello.txt').read().lower())
    return words 

"""



from statistics import mean,median,mode
N = int(input().strip())

# this gets rid of the trailing whitespace before and after the numeric input 

arr = [int(i) for i in input().strip().split(' ')]
arr.sort()

# split the array of numbers into unique numbers and insert into a list 

#print('{0:.1f}'.format(sum(arr)/N))

print(sum(arr)/N)

if N % 2 == 1:
    print(arr[int((N-1)/2)])
else:
    print(0.5*(arr[int(N/2)-1]+arr[int(N/2)]))
    
counts=[]
for i in arr:
    counts.append(arr.count(i))
if max(counts) > 1:
    print(arr[counts.index(max(counts))])
else:
    print(min(arr))

######################################

#Weighted mean excercise 

from statistics import mean,median,mode
N = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]
weighhts = [int(i) for i in input().strip().split(" ")]

count=0
i=0 
weighted=int(arr[i])*int(weights[i])
count=count+weighted
i+=1
print(count)
 
weightedmean=sum()

