class Node:
    def __init__(self, data=None, next=None):
        self.element = data
        self.next = next
        
class Stack:
    head = None
    
    
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new = Node(data)
            new.next = self.head
            self.next = new
    
    def peek(self):
        return self.head.element
    
    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.element = None
        temp.next = None
        