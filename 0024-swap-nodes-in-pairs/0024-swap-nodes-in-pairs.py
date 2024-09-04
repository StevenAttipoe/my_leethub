# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = head.next
        cur = head
        prev = None

        while cur and cur.next:
            a, b, c = cur, cur.next, cur.next.next

            if prev:
                prev.next = b

            b.next = a
            a.next = c

            prev = a
            cur = c

        return newHead

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        a, b, c = head, head.next, head.next.next

        next = self.swapPairs(c)
        
        b.next = a
        a.next = next
        
        return b