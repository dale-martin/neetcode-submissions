# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        return self.split(lists, 0, len(lists) - 1)

    def split(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        m = (l + r) // 2

        return self.merge(self.split(lists, l, m), self.split(lists, m + 1, r))
    
    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return dummy.next