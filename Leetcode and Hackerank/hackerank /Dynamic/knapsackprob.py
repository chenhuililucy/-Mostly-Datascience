
""" 
11 FEB 

Knapsap problem 

""" 


vals=[1,2,3,4]
weights=[1,6,4,5]
capacity=5 


w,h = capacity + 1, len (vals)
table =[ [[0] for y in range (w)] for x in range (h)] #want nested list, initializing table 
print(table)

for index in range(len(vals)):
    for weight in range(w):
        # If the item weights more than the capacity at that column?
        # Take above value, that problem was solved
        if wts[index] > weight:
            table[index][weight] = table[index - 1][weight]
            continue
        
        # if the value of the item < capacity
        prior_value = table[index - 1][weight]
        #         val of current item  + val of remaining weight
        new_option_best = vals[index] + table[index - 1][weight - wts[index]]
        table[index][weight] = max(prior_value, new_option_best)

solution_arr = []

for x in table:
    for y in x:
        solution_arr.append(y)
        
print(max(solution_arr))

max([x for y in table for x in y])

list(range(len(vals)))
