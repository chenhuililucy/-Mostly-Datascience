""" 
first non repeating character 

""" 


string=input()
listchar=[char for char in string]
listchar.sort()

print(listchar)

uniquelistchar=[]
lenchar=[]
a=1
for n in range(len(listchar)-1): 

    if int(n) == int(len(listchar)-2):
        if listchar[n]==listchar[n+1]:
            lenchar.append(a+1)
            uniquelistchar.append(listchar[n])
        else: 
            lenchar.append(a)
            lenchar.append(1)
            uniquelistchar.append(listchar[n])
            uniquelistchar.append(listchar[n+1])

    elif listchar[n]==listchar[n+1]:
        a+=1
            
    else: 
        lenchar.append(a)
        uniquelistchar.append(listchar[n])
        a=1

print(uniquelistchar)
print(lenchar)

dictionary=dict(zip(uniquelistchar,lenchar))

for i in dictionary: 
    if dictionary.get(i)==1: 
        print(i)
        break  



######################



        """
        if listchar[n]==listchar[n+1]:
            lenchar.append(a)
            uniquelistchar.append(listchar[n])
            print(listchar[n])

        else:
            lenchar.append(int(1))
            lenchar.append(int(1))
            uniquelistchar.append(listchar[n])
            uniquelistchar.append(listchar[n+1])
            print(listchar[n])

        """


##########################################################

    def firstNonRepeat(s):
        counter = {}

        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] =  1

        for char in s:
            if counter[char] == 1:
                print (char)
                return

    firstNonRepeat('aabccbdcbe')