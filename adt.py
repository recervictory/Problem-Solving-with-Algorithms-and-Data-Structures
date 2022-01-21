# Complete implementation of the Stack Abstarct data structure
class Stack:
    def __init__(self):
        self.items = []
        self.size = len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size - 1]



    
        
