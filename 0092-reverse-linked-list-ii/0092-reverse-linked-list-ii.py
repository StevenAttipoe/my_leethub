# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = predecessor = ListNode(None, head) 

        for _ in range(left - 1):
            predecessor = predecessor.next

        cur = predecessor.next
        prev = None
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # Connect the reversed sublist back to the main list
        predecessor.next.next = cur
        predecessor.next = prev

        return dummy.next
        