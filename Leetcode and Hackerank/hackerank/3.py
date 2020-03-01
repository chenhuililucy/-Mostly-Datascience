from statistics import mean,median,mode
N = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]
arr.sort()

if N % 2 == 1:
    lowerhalf=arr[:int((N-1)/2)]
    upperhalf=arr[int((N-1)/2):]
    #print(lowerhalf)
else: 
   lowerhalf=arr[:int(N/2)]   
   upperhalf=arr[:int(N/2)]
   #print(lowerhalf)

Nlower=len(lowerhalf)
Nupper=len(upperhalf)

if Nlower % 2 == 1:
    print('{:.0f}'.format(arr[int((Nlower-1)/2)]))
else:
    print('{:.0f}'.format(0.5*(arr[int(Nlower/2)-1]+arr[int(N/2)])))
 

if N % 2 == 1:
    print('{:.0f}'.format(arr[int((N-1)/2)]))
else:
    print('{:.0f}'.format(0.5*(arr[int(N/2)-1]+arr[int(N/2)])))


#need to clear your brain first becore you attempt this ques again  
#Your method is spurious, correct it when you have the time! 
if Nupper % 2 == 1:
    if N % 2 == 1:
        print('{:.0f}'.format(arr[int((Nupper-1)/2)+Nlower+1]))
    else: 
        print('{:.0f}'.format(arr[int((Nupper-1)/2)+Nlower]))

else:
    if N % 2 == 1:
        print('{:.0f}'.format(0.5*(arr[int((Nupper/2)-1+Nlower])))
    else: 
        print('{:.0f}'.format(0.5*(arr[int(Nupper/2)-1+Nlower])))

###########Corrections below#########################


def med(arr):
    arr.sort()
    if len(arr) % 2 == 1:
        ret_value = arr[int((len(arr)-1)/2)]
    else:
        ret_value = 0.5*(arr[int(len(arr)/2-1)]+arr[int(len(arr)/2)])
    return ret_value

N = int(input().strip())

x_arr = [int(i) for i in input().strip().split(' ')]

Q2 = med(x_arr)

l_arr = [i for i in x_arr if i < Q2]
u_arr = [i for i in x_arr if i > Q2]

Q1 = med(l_arr)
Q3 = med(u_arr)

print(int(Q1))
print(int(Q2))
print(int(Q3))