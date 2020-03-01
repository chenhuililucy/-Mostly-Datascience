#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.

"""
def luckBalance():

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')


compilation error when trying to get rid of words

"""



a=re.sub("[^0-9]", "", input())
print(a)
nk = a.split()
print(nk)


n = int(nk[0])

k = int(nk[1])

contests = []

for _ in range(n):
        
        contests.append(list(map(int,a.rstrip().split())))

result = luckBalance(k, contests)


starts1=[]
starts2=[]
for item in contests: 
        if item[1]==1: 
                starts1.append(item[0])
        else: 
                starts2.append(item[0])


stacks=[]

starts1.sort()
for i in range(k): 
        stacks.append(starts1.pop())
print(stacks)
overall=stacks+starts2
a=0 
for i in overall: 
        a+=i

for i in starts1: 
        a-=i


print(a)


