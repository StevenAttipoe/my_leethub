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