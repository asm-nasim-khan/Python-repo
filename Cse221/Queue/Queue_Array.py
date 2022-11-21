class Queue:
    queue = []
    front = 0
    back = -1
    
    def enQueue(self,data):
        self.queue.append(data)
        self.back += 1
    
    def peek(self):
        return self.queue[self.front]
    
    def deQueue(self):
        temp = self.queue[self.front]
        self.queue = self.queue[self.front+1:self.back+1]
        self.back -= 1
        return temp


#Tester Class
q1 = Queue()
q1.enQueue(5)
q1.enQueue(9)
q1.enQueue(10)
#print(q1.peek())
q1.deQueue() # 5
q1.deQueue() # 9
print(q1.peek())       
    
        