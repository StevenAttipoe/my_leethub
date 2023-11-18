# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        setB = set()

        while headA or headB:
            if headA and headB and headA == headB:
                return headA
            
            if headA and headA in setB:
                return headA
            if headB and headB in setA:
                return headB

            if headA: 
                setA.add(headA)
                headA = headA.next

            if headB: 
                setB.add(headB)
                headB = headB.next
        
        return None
        