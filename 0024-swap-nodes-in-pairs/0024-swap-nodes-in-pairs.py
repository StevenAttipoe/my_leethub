# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        prev = None
        cur = head

        while cur and cur.next:
            a = cur
            b = cur.next
            c = cur.next.next

            if prev:
                prev.next = b

            b.next = a
            a.next = c

            prev = a
            cur = c
        return new_head            

