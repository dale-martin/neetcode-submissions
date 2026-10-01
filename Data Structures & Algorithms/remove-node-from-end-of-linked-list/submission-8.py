# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        
        if n == length:
            head = head.next
            return head
        
        i = 0
        node = head
        while node and i < length - n - 1:
            i += 1
            node = node.next

        # node is the node before the one to remove
        node.next = node.next.next

        return head