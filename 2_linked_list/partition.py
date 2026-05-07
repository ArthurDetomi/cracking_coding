from typing import List

from LinkedList import Node


def mergeList(list1: Node, list2: Node):
  currentNode = list1
  
  while currentNode.next != None:
    currentNode = currentNode.next
    
  currentNode.next = list2
  
  return list1


def partition(head: Node, x: int):
    leftList = None
    rightList = None
    
    currentNode = head
    
    currentLeftNode = None
    currentRightNode = None
    
    # O(n)
    while currentNode != None:
      if currentNode.data < x:
        if leftList == None:
          leftList = Node(currentNode.data)
          
          currentLeftNode = leftList
        else:
          currentLeftNode.next = Node(currentNode.data)
          
          currentLeftNode = currentLeftNode.next
      else:
        if rightList == None:
          rightList = Node(currentNode.data)
          
          currentRightNode = rightList
        else:
          currentRightNode.next = Node(currentNode.data)
          
          currentRightNode = currentRightNode.next
           
      currentNode = currentNode.next

    if leftList == None:
      return rightList
    
    if rightList == None:
      return leftList
  
    return mergeList(leftList, rightList)

def partitionBook(node: Node, x: int):
  head = node
  tail = node
  
  while node != None:
    next = node.next
    
    if node.data < x:
      node.next = head
      head = node
    else:
      tail.next = node
      tail = node
    
    node = next
  tail.next = None
  return head

# Input of book
input = Node(3)
input.append(5)
input.append(8)
input.append(5)
input.append(10)
input.append(2)
input.append(1)


newHead = partition(input, 5)

newHead.printNodes()



newHead2 = partitionBook(input, 5)

newHead2.printNodes()


