from Stack import Stack, StackNode
            
class StackWithMin:
    def __init__(self):
        self.head = None
        self.size = 0
        self.auxStack = Stack()
    
    def push(self, val) -> bool:
        newNode = StackNode(val)
        
        self.size += 1
        
        if self.head is None:
            self.head = newNode
            
            self.auxStack.push(val)
            
            return True
        
        if val <= self.auxStack.top():
            self.auxStack.push(val)
        
        aux = self.head
        
        self.head = newNode
        self.head.next = aux
        
        return True
    
    def pop(self):
        if self.head is None:
            raise IndexError("Stack is empty!")
        
        val = self.head.val
        
        if val == self.auxStack.top():
            self.auxStack.pop()
        
        self.size -= 1
            
        aux = self.head.next
    
        self.head = aux
                
        return val
    
    def min(self):
        if self.head is None:
            raise IndexError("Stack is empty!")
        return self.auxStack.top()
    
    def length(self):
        return self.size
    
    def top(self):
        if self.head is None:
            raise IndexError("Stack is empty!")
        return self.head.val
    
stack = StackWithMin()

stack.push(6)
stack.push(5)
stack.push(8)
stack.push(9)
stack.push(1)
stack.push(3)
stack.push(1)
stack.push(1)
stack.push(2)


for _ in range(stack.length()):
    print(f"minimo atual = {stack.min()}, valor do no = {stack.pop()}")