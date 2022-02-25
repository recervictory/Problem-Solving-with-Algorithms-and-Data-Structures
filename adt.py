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


# Completed implementation of a deque ADT

class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def add_front(self,item):
        self.items.append(item)
    
    def add_rear(self,item):
        self.items.insert(0,item)
    
    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items   
