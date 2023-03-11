class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        # Edge case: No value in LL
        if self.head is None:
            self.head = value
            self.tail = value
            self.length = 1
        else:
            # adds the new value to the end of the list
            self.tail.next = new_node
            # makes new value the tail
            self.tail = new_node
            self.length +=1
        return True
        
    def pop(self):
        # Edge Cases
        if self.length ==0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre=temp
            temp = temp.next
        self.tail = pre 
        self.tail.next = None
        self.length -=1 
        if self.length ==0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        pass
    def insert(self, index, value):
        pass
    def remove(self, index):
        pass
    # prints each value in the LinkedList
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
myll = LinkedList(1)
myll.append(2)
myll.print_list()