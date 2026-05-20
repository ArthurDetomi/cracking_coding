from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        slowPointer = head
        fastPointer = head.next

        response = False        
            
        while True:
            if slowPointer.next == None:
                break
            if fastPointer.next == None or fastPointer.next.next == None:
                break
            if slowPointer == fastPointer:
                response = True
                break
            
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            
        
        return response
    
    
# 1 -> 2 -> 3 -> 4 -> None
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

head1 = a

# 1 -> 2 -> 3 -> 4
#           ^    |
#           |____|
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = c  # ciclo

head2 = a

# 1 -> 2 -> 3 -> 4
# ^--------------|

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = a  # ciclo para o começo

head3 = a

# Nó único sem ciclo
a = ListNode(1)

head4 = a

s = Solution()

print(s.hasCycle(head1)) # False
print(s.hasCycle(head2)) # True
print(s.hasCycle(head3)) # True
print(s.hasCycle(head4)) # False


