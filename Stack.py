"""
    
    ###### NOTES #####
    A stack is a collection of objs that are inserted and removed acording to the last-in, first-out (LIFO) principle.
    A user may insert objs into a stack at any time, but may only access or remove the most recently inserted object that
    remains at the "top". 
    The fundamentals involve pushing and popping. 
    
    ###### Adapter Pattern ######
    The adapter design pattern applies to any context where we effectively want to modify an existing class so that its
    methods match those of a related, but different, class or interface. One general way to apply the adapter pattern
    is to define a new class in such a way that contains an instance of the existing class as a hidden field, and then
    to implement each method of the new class using methods of this hidden instance variable. 
    
"""

from queue import Empty

class ArrayStack:
    """
    LIFO Stack implementaion using a Python list as underlying storage
    """
    def __init__(self):
        self._data = []

    def __len__(self):
        # O(1)
        return len(self._data)

    def is_empty(self):
        # O(1)
        return len(self._data) == 0

    def push(self, e):
        # O(1)
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        # O(1)
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Empty Stack")
        # O(1)
        return self._data.pop()


def is_matched(expr):
    """
    Checks if the given expression has matching opening and closing brackets.
    
    Args:
        expr (str): The expression to be checked.
        
    Returns:
        bool: True if the expression has matching brackets, False otherwise.
    """
    lefty = "({["  # Opening brackets
    righty = "]})"  # Closing brackets
    S = ArrayStack()  # Create a new stack
    for c in expr:  # Iterate through each character in the expression
        if c in lefty:  # If the character is an opening bracket
            S.push(c)  # Push it onto the stack
        elif c in righty:  # If the character is a closing bracket
            if S.is_empty():  # If the stack is empty, there is no matching opening bracket
                return False
            if righty.index(c) != lefty.index(S.pop()):  # If the closing bracket doesn't match the last opening bracket
                return False
    return True  # If all brackets match, return True


expression = "({[()]})"
result = is_matched(expression)
print(result)
