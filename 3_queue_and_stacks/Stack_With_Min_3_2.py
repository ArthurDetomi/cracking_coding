class StackNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.min = 0
        
    
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, val) -> bool:
        newNode = StackNode(val)
        
        self.size += 1
        
        if self.head is None:
            newNode.min = val
            self.head = newNode
            return True
        
        aux = self.head
        
        currentMinValue = min(aux.min, newNode.val)
        
        newNode.min = currentMinValue
        self.head = newNode
        self.head.next = aux
        
        return True
    
    def pop(self):
        if self.head is None:
            raise IndexError("Stack is empty!")
        
        val = self.head.val
        
        print("Minimo = ", self.head.min)
        
        self.size -= 1
            
        aux = self.head.next
    
        self.head = aux
        
        
        return val
    
    def min(self):
        return self.head.min
    
    def length(self):
        return self.size
    
stack = Stack()

stack.push(6)
stack.push(5)
stack.push(8)
stack.push(9)
stack.push(1)
stack.push(3)


for _ in range(stack.length()):
    print("Minimo atual = ", stack.min())
    print(stack.pop())