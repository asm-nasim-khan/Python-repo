class Node:
    def __init__(self, data=None, next=None):
        self.element = data
        self.next = next
class Queue:
    head = None
    tail = None
    
    def enQueue(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = self.tail.next
    
    def deQueue(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        temp.element = None
    
    def peek(self):
        return self.head.element
    
#tester class
q1 = Queue()
q1.enQueue(5)
q1.enQueue(9)
q1.enQueue(10)
#print(q1.peek())
q1.deQueue() # 5
q1.deQueue() # 9
print(q1.peek())  
    