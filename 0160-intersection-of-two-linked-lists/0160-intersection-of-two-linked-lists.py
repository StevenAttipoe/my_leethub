# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first = headA
        second = headB

        while first != second:
            first = headB if first.next is None else first.next
            second = headA if second.next is None else second.next

        return first



    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()

        while headA:
            setA.add(headA)
            headA = headA.next

        while  headB:
            if headB in setA:
                return headB
            headB = headB.next
        
        return None
        