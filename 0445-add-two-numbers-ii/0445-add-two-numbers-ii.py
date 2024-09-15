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
        totalSum = 0
        while r1 or r2:
            if r1:
                totalSum += r1.val
                r1 = r1.next
            
            if r2:
                totalSum += r2.val
                r2 = r2.next

            
            r = totalSum // 10
            totalSum = totalSum % 10
            cur.next = ListNode(totalSum)
            totalSum = r
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

