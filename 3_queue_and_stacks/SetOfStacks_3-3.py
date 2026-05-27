from Stack import Stack

class SetOfStacks:
    
    def __init__(self, capacityMax):
        self.stacks = [Stack()]
        self.capacityMax = capacityMax
        self.qtdStacks = 1
    
    def getLastStack(self):
        index = len(self.stacks) - 1
        
        return self.stacks[index]
    
    def push(self, val):
        lastStack = self.getLastStack()
        
        if lastStack.length() == self.capacityMax:
            newStack = Stack()
            
            newStack.push(val)
            
            self.stacks.append(newStack)
            
            self.qtdStacks += 1
        else:
            lastStack.push(val)
        
        for i in range(len(self.stacks)):
            print(self.stacks[i])
        
        return True
    
    def popAt(self, index):
        if index >= self.qtdStacks or index < 0:
            raise IndexError("Stack not found")

        return self.stacks[index].pop()
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty!")
        
        lastStack = self.getLastStack()
        
        while lastStack.isEmpty() and len(self.stacks) > 1:
            self.stacks.pop()
            self.qtdStacks -= 1
            lastStack = self.getLastStack()
            
        response = lastStack.pop()    

        if lastStack.isEmpty():
            self.stacks.pop()
            self.qtdStacks -= 1 
             
        return response
    
    def isEmpty(self):
        return self.qtdStacks == 1 and self.getLastStack().isEmpty()
    
stack = SetOfStacks(3)

stack.push(6)
stack.push(5)
stack.push(8)
stack.push(9)

stack.popAt(0)
stack.popAt(0)
stack.popAt(0)


stack.push(1)
stack.push(3)
stack.push(1)
stack.push(1)
stack.push(2)


while not stack.isEmpty():
    print(f"valor do no = {stack.pop()}")