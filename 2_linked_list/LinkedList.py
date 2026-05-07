class Node:
  def __init__(self, data):
    self.next = None
    self.data = data
  
  def append(self, data):
    currentNode = self
    
    while currentNode.next != None:
      currentNode = currentNode.next
    
    newNode = Node(data)
    
    currentNode.next = newNode
    
  def printNodes(self):
    currentNode = self
    
    nodesData = []
    
    while currentNode != None:
      nodesData.append(currentNode.data)
      
      currentNode = currentNode.next
      
    print(nodesData)
  