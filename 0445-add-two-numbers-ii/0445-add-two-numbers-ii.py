# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)
        
        head = cur = ListNode()
        r = 0
        while r1 or r2:
            a = 0
            b = 0

            if r1:
                a = r1.val
                r1 = r1.next
            
            if r2:
                b = r2.val
                r2 = r2.next

            
            _sum = a + b + r
            if _sum > 9:
                r = _sum // 10
                _sum = _sum % 10
            else:
                r = 0

            cur.next = ListNode(_sum)
            cur = cur.next

        if r:
            cur.next = ListNode(r)

        return self.reverseList(head.next)


    
    def reverseList(self, head):
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

