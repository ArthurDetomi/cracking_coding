from Stack import Stack

class MyQueue:
    def __init__(self):
        self. stackNewest = Stack()
        self.stackOldest = Stack()
        
    def enqueue(self, val):
        self.stackNewest.push(val)
    
    def isEmpty(self):
        return self.stackNewest.isEmpty() and self.stackOldest.isEmpty()
        
    def dequeue(self):
        if not self.stackOldest.isEmpty():
            return self.stackOldest.pop()

        if self.stackNewest.isEmpty():
            raise IndexError("Queue is empty!")
        
        while not self.stackNewest.isEmpty():
            val  = self.stackNewest.pop()
            
            self.stackOldest.push(val)
        
        return self.stackOldest.pop()
    
    def peek(self):
        if not self.stackOldest.isEmpty():
            return self.stackOldest.top()

        if self.stackNewest.isEmpty():
            raise IndexError("Queue is empty!")
        
        while not self.stackNewest.isEmpty():
            val  = self.stackNewest.pop()
            
            self.stackOldest.push(val)
        
        return self.stackOldest.top()

queue = MyQueue()

MAX = 10

for i in range(MAX):
    queue.enqueue(i + 1)

values = []

while not queue.isEmpty():
    val = queue.dequeue()
    values.append(val)
    
print(values)
        
        
        
        
