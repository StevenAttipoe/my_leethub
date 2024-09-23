# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O (N + M) time
    # O(1) space
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next

            elif l1.val >= l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            
            cur = cur.next
        
        cur.next = l1 or l2
        return head.next

    # O (N + M) time
    # O(1) space
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()

        while l1 or l2:
            val1 = l1.val if l1 else math.inf
            val2 = l2.val if l2 else math.inf

            if val1 <= val2:
                cur.next = ListNode(val1)
                l1 = l1.next

            elif val1 >= val2:
                cur.next = ListNode(val2)
                l2 = l2.next

            cur = cur.next
        
        return head.next



        