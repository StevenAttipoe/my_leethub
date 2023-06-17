# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return head

        dummy = head
        endOfFirstHalf = self.getFirstHalfOfList(dummy)
        reversedStartOfSecondHalf = self.reverseList(endOfFirstHalf.next)

        cur = head
        while cur and reversedStartOfSecondHalf:
            if cur == endOfFirstHalf.next:
                break
            if cur.val != reversedStartOfSecondHalf.val:
                return False
            cur = cur.next
            reversedStartOfSecondHalf = reversedStartOfSecondHalf.next
        return True


    def getFirstHalfOfList(self, head):
        slow = fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        cur = head
        prev = None

        while cur:
            adj = cur.next
            cur.next = prev
            prev = cur
            cur = adj
        return prev

        