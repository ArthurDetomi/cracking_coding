class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
  
class Response:
  def __init__(self, tail, size):
    self.tail = tail
    self.size = size  
  
def getTailAndSize(head: ListNode):
    currentNode = head

    size = 0

    tail = currentNode
    while currentNode != None:
        size += 1  

        tail = currentNode
        currentNode = currentNode.next

    return Response(tail, size)

  
def advanceNode(head: ListNode, value):
    currentNode = head
    
    for _ in range(value):
        currentNode = currentNode.next
    
    return currentNode
    
        
# My solution
class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode):
    if headA == None or headB == None:
        return None

    r1: Response = getTailAndSize(headA)
    r2: Response = getTailAndSize(headB)
      
    if (r1.tail != r2.tail):
        return None
      
    largerList = headA if r1.size > r2.size else headB
    shorterList = headB if r1.size > r2.size else headA
      
    advancedNode = advanceNode(largerList, abs(r1.size - r2.size))
    
    currNode1 = advancedNode
    currNode2 = shorterList
    
    while currNode1 != currNode2:
        currNode1 = currNode1.next
        currNode2 = currNode2.next
    
    return currNode1

#Book solution

#Book solution
    

intersect = ListNode(8)
intersect.next = ListNode(10)
intersect.next.next = ListNode(12)

# Lista L1
l1 = ListNode(3)
l1.next = ListNode(7)
l1.next.next = intersect

# Lista L2
l2 = ListNode(99)
l2.next = ListNode(1)
l2.next.next = intersect

s = Solution()
print(s.getIntersectionNode(l1, l2).val)