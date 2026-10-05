# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        dummy = ListNode()
        prev = dummy
        curr = head
        for _ in range(n // k):
            prev.next = self.reverseK(k, curr)
            prev = curr
            curr = curr.next
        
        return dummy.next
        
    def reverseK(self, k, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        b = head

        for i in range(k):
            c = b.next
            b.next = a

            a = b
            b = c

        head.next = c # ???

        return a