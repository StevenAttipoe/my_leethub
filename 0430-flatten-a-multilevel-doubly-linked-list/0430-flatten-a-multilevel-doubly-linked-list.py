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
        
        stack = [head]
        while stack:
            node = stack.pop()
            
            if node.next:
                stack.append(node.next)
                
            if node.child:
                stack.append(node.child)
                node.next = node.child
                node.next.prev = node
                node.child = None
                node = node.next
            else:
                if not node.next and stack:
                    node.next = stack[-1]
                    node.next.prev = node
                    node.child = None
                node = node.next
                
        return head