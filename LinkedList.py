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
        # two pointers
        temp = self.head
        pre = self.head
        # while temp.next is not None
        while(temp.next):
            pre=temp
            temp = temp.next
        # Points to 2nd to last node
        self.tail = pre 
        # break off the last node
        self.tail.next = None
        # decrement size
        self.length -=1 
        # Edge case w/ 1 node
        if self.length ==0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        # Edge case
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1
        return True  
    def pop_first(self):
        # Edge case
        if self.length ==0:
            return None
        else:
            temp = self.head
            # move head pointer
            self.head.next = self.head
            # disconnect old head node
            temp.next = None
            self.length -=1
        return temp
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

    
myll = LinkedList(2)
myll.append(3)
myll.prepend(1)
myll.print_list()
