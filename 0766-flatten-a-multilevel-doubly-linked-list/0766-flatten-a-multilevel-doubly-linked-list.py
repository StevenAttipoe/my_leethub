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

            else:
                if stack:
                    node.next = stack[-1]
                    stack[-1].prev = node

            if node.child:
                stack.append(node.child)
                node.next = node.child
                node.child.prev = node
                node.child = None
                node = node.next                

        return head
        