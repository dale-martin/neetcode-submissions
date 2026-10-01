# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        a = head
        b = a.next
        a.next = None

        if not b:
            return head

        while b.next:
            c = b.next
            b.next = a

            a = b
            b = c

        b.next = a
        return b