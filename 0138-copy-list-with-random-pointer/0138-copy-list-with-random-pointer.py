"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
            
        #Sandwich copyNodes betweent oldNodes
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        #Set random pointers for copy nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next

        #Unweave list
        oldList = head
        newList = head.next
        newHead = head.next
        while oldList:
            oldList.next = oldList.next.next
            if newList.next:
                newList.next = newList.next.next
            else:
                 newList.next = None
            oldList = oldList.next
            newList = newList.next

        return newHead