"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        dummy = Node(0)
        curr, stack = dummy, [head]
        
        while stack:
            topNode = stack.pop()
            
            if topNode.next:
                stack.append(topNode.next)
                
            if topNode.child:
                stack.append(topNode.child)
                
            curr.next = topNode
            topNode.prev = curr
            topNode.child = None
            curr = topNode
            
        dummy.next.prev = None
        return dummy.next
            