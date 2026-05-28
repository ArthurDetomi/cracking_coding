from Stack import Stack

class MyQueue:
    def __init__(self):
        self.stackNewest = Stack()
        self.stackOldest = Stack()
        
    def enqueue(self, val):
        return self.stackNewest.push(val)
    
    def isEmpty(self):
        return self.stackNewest.isEmpty() and self.stackOldest.isEmpty() 
    
    # if stackOldest not is Empty O(1) else O(len(stackNewest))
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        
        if self.stackOldest.isEmpty():
            while not self.stackNewest.isEmpty():
                val = self.stackNewest.pop()
                self.stackOldest.push(val)
                
        return self.stackOldest.pop()
    
    # if stackOldest not is Empty O(1) else O(len(stackNewest))
    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        
        if self.stackOldest.isEmpty():
            while not self.stackNewest.isEmpty():
                val = self.stackNewest.pop()
                self.stackOldest.push(val)
                
        return self.stackOldest.top()
    
queue = MyQueue()

for i in range(10):
    queue.enqueue(i)

queue.dequeue()

queue.dequeue()

queue.dequeue()

queue.dequeue()

queue.enqueue(10)

while not queue.isEmpty():
    print(queue.dequeue())