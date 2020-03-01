
""" 
11 FEB 
Dynamic programming example 
Hackerrank medium difficulty 

""" 

# My answer: did not consider the case whereby the lowercase is between the uppercases 

import math
import os
import random
import re
import sys


q = int(input())

for q_itr in range(q):
    a = input()

    b = input()

    if b in a.upper():
        new=a.upper()
        index1=new.find(b)
        index2=index1+len(b)
        newstring1 = a[0 : index1 : ] 
        removed1= re.sub( "[a-z]", "", newstring1)
        newstring2 = a[index2: :]
        removed2= re.sub( "[a-z]", "", newstring2)
        finalstring=removed1+b+removed2
        if finalstring==b:

            print("YES")
        else: 
            print("NO")
    
    else: 
        print("NO")



######################################################################################

#model answer 


for _ in xrange(int(input())):
    src = raw_input()
    des = raw_input()
    i,j= 0,0
    while True:
        if i == len(src):
            if j == len(des):
                print 'YES'
            else:
                print 'NO'
            break
        if j == len(des):
            a = src[i:]
            b = src[i:]
            if a.lower() == b:
                print 'YES'
            else:
                print 'NO'
            break
        if src[i].isupper():
            if des[j] != src[i]: # case whereby 
                print 'NO'
                break
            else:
                i+=1
                j+=1
        elif src[i].upper() == des[j]:
            k = i+1
            flag=True
            for x in range(k,len(src)):
                if src[x].upper() == des[j]:
                    flag = False
                    break
                    
            if flag:
                i+=1
                j+=1
            else:
                i+=1
        else:
            i+=1
            