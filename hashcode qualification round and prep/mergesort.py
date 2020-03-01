def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
        print ("hello")
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]

    print(left_list)

    right_list = unsorted_list[middle:]

    print(right_list)

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    print(left_list)
    print("l")
    print(right_list)
    print("r")
    return list(merge(left_list, right_list))
    

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [1, 34, 25, 12, 22, 11, 90]

print(merge_sort(unsorted_list))

""" 
[1, 34, 25]
[12, 22, 11, 90]
[1]
[34, 25]
[34]
[25]
[34]
l
[25]
r
[1]
l
[25, 34]
r
[12, 22]
[11, 90]
[12]
[22]
[12]
l
[22]
r
[11]
[90]
[11]
l
[90]
r
[12, 22]
l
[11, 90]
r
[1, 25, 34]
l
[11, 12, 22, 90]
r
[1, 11, 12, 22, 25, 34, 90]



"""