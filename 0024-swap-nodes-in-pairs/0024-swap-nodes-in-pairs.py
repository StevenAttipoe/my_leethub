# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur = head
        newHead = head.next
        prev = None
        while cur and cur.next:
            a, b = cur, cur.next
            if prev:
                prev.next = b
            b.next, a.next = a, b.next
            prev = a 
            cur = cur.next

        return newHead
            # 1 -- 2 -- 3 -- 4
            # 2 -- 1 -- 3 -- 4
            # 2 -- 1 -- 4 -- 3


            # 0 -- 1 -- 2 -- 3 -- 4 -- 5
            # 0 -- 2 -- 1 -- 3 -- 4 -- 5
            # 0 -- 2 -- 1 -- 4 -- 3 -- 5

            # 0 -- 1 -- 2 -- 3 -- 4 -- 5 -- 6
        

        