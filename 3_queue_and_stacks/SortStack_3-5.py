from Stack import Stack

import random

class SortStack():
    def __init__(self):
        self.stack = Stack()
    
    def isEmpty(self):
        return self.stack.isEmpty()
    
    def peek(self):
        return self.stack.top()
    
    def pop(self):
        return self.stack.pop()
    
    def push(self, val):
        auxStack = Stack()

        while not self.stack.isEmpty() and self.peek() < val:
            auxStack.push(self.stack.pop())

        self.stack.push(val)

        while not auxStack.isEmpty():
            self.stack.push(auxStack.pop())
    

QTD = 10


sortStack = SortStack()

for _ in range(QTD):
    num = random.randint(1, 20)
    print("Aleatorio = ", num)
    sortStack.push(num)
    
while not sortStack.isEmpty():
    v = sortStack.pop()
    
    print(v)
    
    
    