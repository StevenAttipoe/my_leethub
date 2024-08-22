# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        newHead = head.next
        prev, cur = None, head

        while cur and cur.next:
            a = cur
            b = cur.next
            c = cur.next.next

            b.next = a
            a.next = c

            if prev:
                prev.next = b

            prev = a
            cur = c
        return newHead            

			
            
        