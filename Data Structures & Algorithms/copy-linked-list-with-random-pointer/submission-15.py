"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        while curr is not None:
            curr.next = Node(curr.val, curr.next, None)
            curr = curr.next.next
        
        curr = head
        while curr is not None:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        dummy = Node(0)
        newListCurr = dummy
        curr = head
        while curr is not None:
            newListCurr.next = curr.next
            newListCurr = newListCurr.next

            curr.next = curr.next.next
            curr = curr.next
        
        return dummy.next