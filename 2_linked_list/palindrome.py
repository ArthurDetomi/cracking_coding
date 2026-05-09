from LinkedList import Node

def palindrome(li: Node):
  if li == None:
    return False

  currNode = li
  
  stack = []
  
  while currNode != None:
    stack.append(currNode.data)
    
    currNode = currNode.next
  
  currNode = li
  
  while currNode != None:
    if stack.pop() != currNode.data:
      return False
    
    currNode = currNode.next  
  
  return True
 
def reverseAndClone(node: Node):
  head = None
  
  while node != None:
    n = Node(node.data)
    n.next = head
    head = n
    node = node.next
  
  return head

def isEqual(node1 :Node, node2 :Node):
  if node1 == None or node2 == None:
    return False
  
  while node1 != None:
    if node1.data != node2.data:
      return False
    
    node1 = node1.next
    node2 = node2.next
    
  return True

def isPalindromeBook(li: Node):
  reversed = reverseAndClone(li)
  return isEqual(li, reversed)


l1 = Node(7)
l1.append(1)
l1.append(6)


print(palindrome(l1))

print("Palindrome book", isPalindromeBook(l1))

l2 = Node(0)
l2.append(1)
l2.append(2)
l2.append(1)
l2.append(0)

print(palindrome(l2))

print("Palindrome book", isPalindromeBook(l2))