from statistics import mean,median,mode
N = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]
#print(arr)
weights = [int(i) for i in input().strip().split(" ")]
#print(weights)

count=0
i=0 
for i in range(N): 
    weighted=int(arr[i])*int(weights[i])
    #print(weighted)
    count=count+weighted
    i=i+1
    #print(i)

# key: python formating to one decimal place 
print(1
format(count/sum(weights)))



""""


N = int(input().strip())

x_arr = [int(i) for i in input().strip().split(' ')]
w_arr = [int(i) for i in input().strip().split(' ')]

run_sum = 0
for i in range(N):
    run_sum += x_arr[i]*w_arr[i]
    
print('{0:.1f}'.format(run_sum/sum(w_arr)))
"""
