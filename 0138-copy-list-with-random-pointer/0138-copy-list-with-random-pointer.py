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
        cur = head
        nodeToCopy = {}
        
        while cur:
            nodeToCopy[cur] = Node(cur.val)
            cur = cur.next
            
        cur = head
        while cur:
            copy = nodeToCopy[cur]
            copy.next = nodeToCopy.get(cur.next, None)
            copy.random = nodeToCopy.get(cur.random, None)
            cur = cur.next
            
        return nodeToCopy.get(head, None)
            
        