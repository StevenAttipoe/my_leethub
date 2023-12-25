# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        prev, cur = None, head
        while cur:
            if cur.val == val:
                if head.val == cur.val:
                    head = head.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        prev, cur = dummy, dummy.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
            
        return dummy.next

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            
        return dummy.next




        
