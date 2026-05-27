class StackNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, val) -> bool:
        newNode = StackNode(val)
        
        self.size += 1
        
        if self.head is None:
            self.head = newNode
            return True
        
        aux = self.head
        self.head = newNode
        self.head.next = aux
        
        return True
    
    def pop(self):
        if self.head is None:
            raise IndexError("Stack is empty!")
        
        val = self.head.val
        
        self.size -= 1
            
        aux = self.head.next
    
        self.head = aux
        
        return val
    
    def length(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0 
    
    def top(self):
        if self.head is None:
            raise IndexError("Stack is empty!")
        return self.head.val
    
    def __str__(self):
        values = []
        
        currentNode = self.head
        
        while currentNode != None:
            values.append(currentNode.val)
            currentNode = currentNode.next
            
        return f"{values}"