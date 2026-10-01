# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        b = slow.next
        a = slow.next = None
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        
        a, b = head, a
        while b:
            c, d = a.next, b.next
            a.next = b
            b.next = c
            a, b = c, d