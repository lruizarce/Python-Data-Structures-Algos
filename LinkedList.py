class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.legth = 1
        
    def append(self, value):
        pass
    def pop(self):
        pass
    def prepend(self, value):
        pass
    def insert(self, index, value):
        pass
    def remove(self, index):
        pass
    
class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None
    
