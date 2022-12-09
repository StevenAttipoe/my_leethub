"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur = root
        while cur and cur.left:
            nxt = cur.left
            while cur:
                cur.left.next = cur.right
                cur.right.next = cur.next.left if cur.next else None
                cur = cur.next
            cur = nxt
        return root
        