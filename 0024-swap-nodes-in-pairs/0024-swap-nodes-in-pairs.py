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
        head.next = self.swapPairs(head.next.next)
        newHead.next = head

        return newHead

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur, newHead = head, head.next
        prev = None

        while cur and cur.next:
            a, b, c = cur, cur.next, cur.next.next

            if prev:
                prev.next = b

            self.swap(a, b, c)

            prev = a
            cur = c
            
        return newHead

    def swap(self, a, b, c):
        b.next = a
        a.next = c
# 1 -> 2 -> 3 -> 4
# 2 -> 1 -> 3 -> 4
# 2 -> 1 -> 4 -> 3
        
        