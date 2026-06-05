class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def isEmpty(self):
        return self.head == None
    
    def enqueue(self, val) -> bool:
        newNode = QueueNode(val)
        
        self.size += 1
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return True

        self.tail.next = newNode
        self.tail = newNode 
    
        return True   
        
    def dequeue(self):
        if self.head == None:
            raise IndexError("Queue is empty")
        
        self.size -= 1
        
        val = self.head.val
        
        if self.head.next == None:
            self.head = None
            self.tail = None
            return val
        
        self.head = self.head.next
        
        return val

    def length(self):
        return self.size
    
queue = Queue()

for i in range(1, 12):
    queue.enqueue(i)

for i in range(1, 12):
    print(f"tamanho = {queue.length()}")
    print(queue.dequeue())

print("Segunda vez:")

for i in range(1, 12):
    queue.enqueue(i)

for i in range(1, 12):
    print(f"tamanho = {queue.length()}")
    print(queue.dequeue())



       