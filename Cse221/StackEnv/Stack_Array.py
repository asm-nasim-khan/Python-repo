class Stack:
    stack = []
    pointer = -1
    
    def push(self,element):
        self.stack.append(element)
        self.pointer += 1
    
    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return value
        
    def peek(self):
        return(self.stack[self.pointer])
    
#Tester Class
Stack1 = Stack()
Stack1.push(2)
print(Stack1.peek())
Stack1.push(5)
print(Stack1.pop())
print(Stack1.peek())
        