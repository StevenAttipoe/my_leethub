"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
            
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            n = len(queue)
            level = []

            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            res.append(level)

        return res
                
        