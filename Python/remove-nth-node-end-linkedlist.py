# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        sz = 1
        cur = head
        while cur.next:
            cur = cur.next
            sz += 1

        if sz == 1: return None
        if sz == n:
            head = head.next
            return head

        prev, cur = head, head.next
        for i in range(sz - n - 1):
            prev = prev.next
            cur = cur.next
        
        prev.next = cur.next
        cur.next = None

        return head
        