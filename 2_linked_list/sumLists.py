from LinkedList import Node

def sumList(l1: Node, l2: Node):
  if l1 == None:
    return l2
  if l2 == None:
    return l1

  currNode1 = l1
  currNode2 = l2

  resultList = None
  currResultList = None
  
  carry = 0
  
  while currNode1 != None or currNode2 != None:
    value1 = 0 if currNode1 == None else currNode1.data
    
    value2 = 0 if currNode2 == None else currNode2.data
    
    sumResult = value1 + value2 + carry
    
    if sumResult >= 10:
      carry = 1
      sumResult -= 10
    else:
      carry = 0

    if resultList == None:
      resultList = Node(sumResult)
      
      currResultList = resultList
    else:
      currResultList.next = Node(sumResult)
      
      currResultList = currResultList.next
    
    if currNode1 != None:  
      currNode1 = currNode1.next
    if currNode2 != None:
      currNode2 = currNode2.next  
      
  if carry == 1:
    currResultList.next = Node(1)
  
  return resultList

l1 = Node(7)
l1.append(1)
l1.append(6)

l2 = Node(5)
l2.append(9)
l2.append(2)

result = sumList(l1, l2)

result.printNodes()

l1 = Node(0)
l1.append(9)



l2 = Node(0)
l2.append(9)

result = sumList(l1, l2)

result.printNodes()
