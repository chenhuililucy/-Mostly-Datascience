


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
        if target==data[mid]: 
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
    def __init__(self,data=None, next_node=None): 
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
        self.head = head # the head node is the top node in the list, when the list is first initialized, it had 0 nodes
        
    def insert(self,data): 
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node 
    
    def size(self):
        current= self.head 
        count=0
        while current:
            count+=1 
            current=current.get_next()
        return count 

    def search(self,data): 
        current=self.head 
        found=False 
        while current and found is False: 
            if current.get_data()==data: 
                found = True
            else: 
                current=current.get_next()
        if current is None: 
            raise ValueError("Data not in list")
        return current

    def delete(self,data): 
        current=self.head 
        previous=None
        found=False 
        while current and found is False: 
            if current.get_data()==data: 
                found=True
            else: 
                current=current.get_next()
        if current is None: 
            raise ValueError("Data not in list")
        if previous is None: 
            self.head=current.get_next()
        else: 
            previous.set_next(current.get_next()) 


                

########################
########################
########################




    

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next



Node1=ListNode(1)
Node2=ListNode(2)
Node3=ListNode(3)
Node4=ListNode(4)
Node5=ListNode(5)
Node6=ListNode(6)
Node7=ListNode(7)
Node8=ListNode(8)
Node9=ListNode(9)


# Node1.next=Node2 
# Node2.next=Node3
# Node3.next=Node4
# Node4.next=Node5


Linkedlist1 = MyLinkedList()


Linkedlist1.addAtTail(1)
Linkedlist1.addAtTail(2)
Linkedlist1.addAtTail(3)


print(Linkedlist1.get(2))