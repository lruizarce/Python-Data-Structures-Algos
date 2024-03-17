##### NOTES #####

"""
Another fundamental data structure is the queue. It is a close "cousin" of the stack,
as a queue is a collection of objs that are inserted and removed according to the
first-in, first-out (FIFO) principle.
Elements can be inserted at any time, but only the element that has been in the queue the longest can be next removed.
Think about a line of people waiting to get on a ride. 
"""
    
    
from queue import Empty
class ArrayQueue:
    DEFAULT_CAP = 10
    
    def __init__(self):
        """Initialize an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAP
        self._size = 0
        self._front = 0 
        
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self._size) == 0
    
    def first(self):
        """Return the first element in the queue without removing it.
        
        Raises:
            Empty: If the queue is empty.
        """
        if self.is_empty():
            raise Empty("Empty Q")
        return self._data[self._front]
    
    def dequeue(self):
        """Remove and return the first element of the queue.
        
        Raises:
            Empty: If the queue is empty.
        """
        if self.is_empty():
            raise Empty('Empty Q')
        # assigns answer to the value of the current index
        answer = self._data[self._front]
        # deattaches current index and assigns it to None
        self._data[self._front] = None
        # update index of the front
        self._front = (self._front + 1) % len(self._data)
        # decreases size of our Q
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            # double the array size using the lenght of the data
            self._size(2 * len(self.data))
        # locate the next available location
        avail = (self._front + self.size) % len(self._data)
        # add new element at the next available index
        self._data[avail] = e
        # increase the size of the queue
        self._size +=1 
        
    def resize(self, cap):
        # keep track of old list
        old = self._data
        # creates new list with the new capacity
        self._data = [None] * cap
        # assigns walk to the front
        walk = self._front
        # iterates through the 
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0