
"""
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. 
The first line of each test case is N and S, 
where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.
Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.
Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010
Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5
Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15


"""
    #=================brute force(quadratic time complexity)=================#

def subArraySum1(array,N,S): 
    BOOLEAN=True
    for a in range(N):
        for i in range(1,N):
            subarray=array[a:a+i]
            intendedsum=sum(subarray)
            if intendedsum==S:
                print(a+1,a+i)
                BOOLEAN=False
                break
        if not BOOLEAN: 
            break 
    if BOOLEAN:
        print("-1")
     #=================Efficient(linear time complexity)=================#

def subArraySum(arr, n, sum): 
       
    curr_sum = arr[0] 
    start = 0
    i = 1
    while i <= n: 
        while curr_sum > sum and start < i-1: #assert current index greater than start
            curr_sum = curr_sum - arr[start] 
            start += 1 
        if curr_sum == sum: 
            print (start+1, i) 
            return 1
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
    #=================input=================#

testcases=int(input())

for i in range(testcases):
    n=[int(x) for x in input().split()] 
    N=n[0]
    S=n[1]  
    arr1=[int(x) for x in input().split()]
    subArraySum(arr1,N,S)
    subArraySum1(arr1,N,S)