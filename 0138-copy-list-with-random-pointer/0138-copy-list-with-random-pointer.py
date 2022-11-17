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
        nodeToCopy = {None: None}
        
        while cur:
            nodeToCopy[cur] = Node(cur.val)
            cur = cur.next
            
        cur = head
        while cur:
            copy = nodeToCopy[cur]
            copy.next = nodeToCopy[cur.next]
            copy.random = nodeToCopy[cur.random]
            cur = cur.next
            
        return nodeToCopy[head]
            
        