""" 
K closest to origin 

""" 


# nestedlists=input()

# biglist=[]
# euclideandislist=[]

# for item in nestedlists: 
#     biglist.append(item)
#     print(item)
#     euclideandis=item[0]*item[1]
#     euclideandislist.append(euclideandis)

# dic=dict(zip(euclideandislist,biglist)) 
# sorted_x = sorted(dic.items([[1,3],[-2,2]]), key=operator.itemgetter(0))
            



# class Solution(object):
#     def kClosest(self, points, K):


#         euclideandis=((points[0]**2)+(points[1]**2))**0.5
#         dict={[points[0],points[1]] : euclideandis for item in list }


#         points.sort(key = lambda P: P[0]**2 + P[1]**2)
#         return points[:K]


# class Solution(object):
    

        
#     def kClosest(self, points, K):

#         for num in points:

#             dict={ [num[0], num[1]] : euclideandis }
            
#                 def gendis(kClosest):
    
#         euclideandis=((num[0]**2)+(num[1]**2))**0.5
        
#         return euclideandis


class Solution(object):
    

        
    def kClosest(self, points, K):

        
        list1=[] 
        list2=[]
        for num in points:
            list1.append(num)
            list2.append(num[0]**2+num[1]**2)
        
        dictionary=dict(zip(list1,list2))
        sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
        return min(dict.items(), key=lambda x: x[1]) 



class Solution(object):
    

        
    def kClosest(self, points, K):

        
        list1=[] 
        list2=[]
        for num in points:
            list1.append(num)
            list2.append(num[0]**2+num[1]**2)
        
        dictionary=dict(zip(list1,list2))
        sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
        print(min(dict.items(), key=lambda x: x[1]) )
        return min(dict.items(), key=lambda x: x[1]) 


####################


class Solution(object):
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1


            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]