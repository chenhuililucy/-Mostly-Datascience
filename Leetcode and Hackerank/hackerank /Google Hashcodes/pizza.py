



x="/Users/lucy/Desktop/assortedcodes/e_also_big.in"

with open(x,"r") as file: 
    filedata=file.readlines()
    max, types = filedata[0].rstrip().split(" ")
    max=int(max)
    types=int(types)
    a=0
    list=[]
    for i in range(types):
        if a<max: 
            listnum=filedata[1].split(" ")
            listnum.sort(reverse=True)
            b=listnum.pop(i)
            a+=int(b)
            if a<max:
                list.append(i)
            else: 
                a-=int(b)
                excess=max-a

            """
                BOOLEAN=True 
                #while a<max:
                for n in range(len(listnum)-2):
                    a+=int(listnum.pop(n))
                    if a<max: 
                        BOOLEAN=False 
                        list.append(n)
                    if BOOLEAN:
                        pass

            """

    #print(list)
    submit = open("output_"+x,"w+")
    submit.write(str(len(types))+"\n")
    for a in buying_pizzatypes:
		submit.write(str(a)+" ")
	submit.close()


    print(max)
    print(a)



        



