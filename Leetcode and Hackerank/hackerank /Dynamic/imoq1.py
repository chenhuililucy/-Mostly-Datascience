

k=10000 # for n is any integer greater than 1 
steps=k+10000

def funcgen():
    list=[]

    for n in range(1,k): 

        list.append([])
        if n==1:
            list.append([])


        for a in range(1,k): #for each of this, we generate a set of new list 

            b=0
            BOOLEAN=True

            while BOOLEAN: 
            
                if (a**0.5).is_integer(): 
                    a=a**0.5
                    list[n].append(a)
                    b+=1 
                    continue 
                    if b>steps: 
                        BOOLEAN=False  

                    
                else: 
                    a+=3 
                    list[n].append(a)
                    b+=1 
                    continue

                    if b>steps: 
                    
                        BOOLEAN=False  
 

                continue
                
    
    print(list)

    final=set.intersection(*map(set, list))

    print(final)


funcgen()