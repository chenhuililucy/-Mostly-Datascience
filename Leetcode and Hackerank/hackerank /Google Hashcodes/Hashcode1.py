





import heapq

x="/Users/lucy/Desktop/assortedcodes/a_example.txt" #modify directory 


########Reading in file############
count=0
with open(x,"r") as file: 

    for line in file: 
        count+=1 
    
    count-=3

with open(x,"r") as file: 

    filedata=file.readlines()
    #print(filedata)
    items=filedata[0].rstrip().split(" ")
    B=items[0] #no of different books 
    L=items[1] #no of libraries
    D=items[2] #no of days
    Bookscores=filedata[1].rstrip().split(" ")
    #Bookscoresum=sum(int(i) for i in Bookscores)
    
    noofbooksall=[]
    signupdaysall=[]
    shippingdaysall=[]
    IDsall=[]
    Bookscoresumtotal=[]
    for i in range(0,count,2):
        noofbooks,signupdays,shippingdays = filedata[2+i].rstrip().split(" ")
        noofbooksall.append(noofbooks)

        #Bookscoresum=sum(int(noofbooks) for noofbooks in Bookscores[init:noofbooks]) FUCK
        
        Bookscoresumtotal.append(Bookscoresum)
        print(Bookscoresumtotal)
        signupdaysall.append(signupdays)
        shippingdaysall.append(shippingdays)
        IDs = filedata[3+i].rstrip().split(" ")
        IDsall.append(IDs)
        #print(IDsall) #nested list
        #print(signupdaysall)
        count=0 
        for item in noofbooksall: 
            Bookscoresum.append(item)
        
            
    a=signupdaysall


def sortsum(): 
    new=Bookscoresumtotal.sort()
    print(new)
    # for i in new: 
    #     newindex=Bookscoresumtotal.index(i)

sortsum()


# Want: start from the lowest signup time, get index of pop sequence 

signupheap=heapq.heapify(signupdaysall)
indexlist=[]
sortedsignupdays=[]
for i in signupdaysall:  
    sortedsignupdays.append(heapq.heappop(signupdaysall))
    #l=signupdaysall.index(heapq.heappop(signupdaysall))
for i in signupdaysall: 
    sortedsignupdays.append(i)
#print(sortedsignupdays)
    #indexlist.append(signupdaysall.index(heapq.heappop(signupdaysall)))

with open(x,"r") as file: 

    filedata=file.readlines()
    #print(filedata)
    items=filedata[0].rstrip().split(" ")
    B=items[0]
    L=items[1]
    D=items[2]
    Bookscores=filedata[1].rstrip().split(" ")
    
    noofbooksall=[]
    signupdaysall=[]
    shippingdaysall=[]
    IDsall=[]
    for i in range(0,count,2):
        noofbooks,signupdays,shippingdays = filedata[2+i].rstrip().split(" ")
        noofbooksall.append(noofbooks)
        signupdaysall.append(signupdays)
        shippingdaysall.append(shippingdays)
        IDs = filedata[3+i].rstrip().split(" ")
        IDsall.append(IDs)
        #print(IDsall) #nested list
    #print(signupdaysall)
    a=signupdaysall

for i in sortedsignupdays: 
    #print(a)
    #print(str(i))
    #print(a)
    indexlist.append(a.index(str(i)))
temp=[]
count=0
for i in sortedsignupdays:
    count+=int(i)
    temp.append(count)
  

moredays=[]
for i in indexlist: 
    if int(noofbooksall[i])%int(shippingdaysall[i])==0: 
        moredays.append(int(noofbooksall[i])/int(shippingdaysall[i]))
    else: 
        moredays.append(int(noofbooksall[i])//int(shippingdaysall[i])+int(1))
    #print(moredays)


for i in moredays: 
    for a in temp: 
        sumdays=0
        totaldays=int(i)+int(a)
        if totaldays>sumdays:
            sumdays=totaldays
        else: 
            break 

        if totaldays > int(D): 
            break 

#def maxbook(): 




"""

submit = open("output_"+x,"w+")
    submit.write(str(len(types))+"\n")
    for a in buying_pizzatypes:
		submit.write(str(a)+" ")
	submit.close()

"""
