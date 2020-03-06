


""" 
Binary search

""" 

data=[2,3,4,4,6,7,7,8]
target=1


#iterative binary search
def binary_search_iterative(data,target): 
    low=0 
    high=len(data)-1

    while low<=high:
        mid=(low+high)//2
        if target=data[mid]: 
            return True 
        elif target<data[mid]: 
            high=mid-1
        else: 
            low=mid+1 

    return False 


#recursive binary search 

def binary_search_recursive(data,target,low, high): 
    if low<high:
        return False
    else: 
        mid = (low+high)//2 
        if target==data[mid]: 
            return True
        elif target<data[mid]: 
            return binary_search_recursive(data,target,low, mid-1)
        else:
            return binary_search_recursive(data,target,mid+1, high)
        


#############################


#initializing a single datum and the pointer is set to None by default 
#first node inserted into the list has nothing to point to at all  



""" 
insert: inserts a new node into the list 
size: returns size of a list 
search: searches list for a node containing the requested data and returns node if found, otherwise raises error 
delete: searhces list for a node containing the requested data and removes it from the list if found, otherwise raises error 
""" 

class Node(object): 
    def__init__(self.data=None, next_node=None): 
        self.data=data 
        self.next_node=next_node
    
    def get_data(self): # returns data 
        return self.data 

    def get_next(self): # returns the next node 
        return self.next_node

     def set_next(self, new_next): # method to reset the pointer to a new node 
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def insert(self,data): 
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node 
    
    