class MultiStack:
    def __init__(self, stackSize):
        self.values = [0 for _ in range(stackSize * 3)]
        self.sizes = [0 for _ in range(3)]
        self.stackCapacity = stackSize * 3
        self.maxSizeStack = stackSize


    def getSize(self, stackSelected):
        if stackSelected >= 3 or stackSelected < 0:
            raise KeyError()
        return self.sizes[stackSelected]
    
    def _getBeginStack(self, stackSelected):
        if stackSelected >= 3 or stackSelected < 0:
            raise KeyError()
        
        if stackSelected == 0:
            return 0
        
        return int(stackSelected * (self.stackCapacity / 3)) 
    
    def push(self, val, stackSelected) -> bool:
        sizeStack = self.getSize(stackSelected)
        
        if sizeStack == self.maxSizeStack:
            return False
             
        pos = self._getBeginStack(stackSelected) + sizeStack      

        self.values[pos] = val
        self.sizes[stackSelected] += 1
        
        return True
    
    
    def isEmpty(self, stackSelected) -> bool:
        return self.getSize(stackSelected) == 0
    
    def pop(self, stackSelected):
        sizeStack = self.getSize(stackSelected)
        
        if self.isEmpty(stackSelected):
            raise RuntimeError("Is empty stack")
        
        pos = self._getBeginStack(stackSelected) + sizeStack      
  
        self.sizes[stackSelected] -= 1
        return self.values[pos - 1]

size = 4
multiStack = MultiStack(size)

print("Stack 1")
for i in range(size):
    multiStack.push(i, 0)

for i in range(size):
    print(multiStack.pop(0))


print("Stack 2")
for i in range(size):
    multiStack.push(i, 1)

for i in range(size):
    print(multiStack.pop(1))
        

print("Stack 3")
for i in range(size):
    multiStack.push(i, 2)

for i in range(size):
    print(multiStack.pop(2))
    


print("Tamanhos finais")
for i in range(3):
    print(multiStack.sizes[i])
            