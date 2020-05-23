
import csv

a=["价格"]
b=["递增"]
f=["平米"]
c=["总数"]
d=["每年总数"]
ei=["每月总数"]



area=35479
days=365 
price=[1.5,1.55,1.6,1.65,1.70,1.75,1.80]
increment=1
i=3
s=0



for element in price:
    first=1
    for e in range(20):
        s+=area*days*element
    #print("价格")
    #print(element)
    a.append(element)
    #print("递增")
    #print(increment-1)
    b.append(increment-1)
    #print("总数")
    #print(s)
    c.append(s)
    #print("每年总数")
    #print(str(s/20))
    d.append(str(s/20))
    #print("每月总数")
    #print(s/20/12)
    ei.append(str(s/20/12))
    f.append(area)
    s=0


area=35479
days=365 
price=[1.5,1.55,1.6,1.65,1.70,1.75,1.80]
increment=1.05
i=3
s=0
first=1

for element in price:
    first=1
    for e in range(20):
        if i==0:
            first*=increment
            s+=area*days*element*first
            i=2
        else:
            s+=area*days*element*first
            i-=1
    #print("价格")
    #print(element)
    a.append(element)
    #print("递增")
    #print(increment-1)
    b.append(increment-1)
    #print("总数")
    #print(s)
    c.append(s)
    #print("每年总数")
    #print(str(s/20))
    d.append(str(s/20))
    #print("每月总数")
    #print(s/20/12)
    ei.append(str(s/20/12))
    f.append(area)
    s=0





area=42820
days=365 
price=[1.2,1.3,1.4,1.5]
increment=1.00
i=3
s=0
first=1

for element in price:
    first=1
    for e in range(20):
        s+=area*days*element
    #print("价格")
    #print(element)
    a.append(element)
    #print("递增")
    #print(increment-1)
    b.append(increment-1)
    #print("总数")
    #print(s)
    c.append(s)
    #print("每年总数")
    #print(s/20)
    d.append(s/20)
    #print("每月总数")
    #print(s/20/12)
    ei.append(str(s/20/12))
    f.append(area)
    s=0


area=42820

days=365 
price=[1.2,1.3,1.4,1.5]
increment=1.05
i=3
s=0
first=1

for element in price:
    first=1
    for e in range(20):
        if i==0:
            first*=increment
            s+=area*days*element*first
            print(area*days*element*first)
            i=2 
        else:
            s+=area*days*element*first
            print(area*days*element*first)
            i-=1
    #print("价格")
    #print(element)
    a.append(element)
    #print("递增")
    #print(increment-1)
    b.append(increment-1)
    #print("总数")
    #print(s)
    c.append(s)
    #print("每年总数")
    #print(s/20)
    d.append(s/20)
    #print("每月总数")
    #print(s/20/12)
    ei.append(str(s/20/12))
    f.append(area)
    s=0


z=zip(a,b,f,c,d,ei)
with open("rent.csv","w") as csvfile:
    wr=csv.writer(csvfile)
    for element in z:
        wr.writerow(element)