# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        plane = defaultdict(list)
        queue = deque([(root, (0, 0))])

        while queue:
            node, (x, y) = queue.popleft()

            plane[(x, y)].append(node.val)
            plane[(x, y)].sort()

            if node.left:
                queue.append((node.left, (x + 1, y - 1)))
            
            if node.right:
                queue.append((node.right, (x + 1, y + 1)))
        
        sortedKeys = sorted(plane.keys(), key = lambda k: (k[1], k[0]))
        yPlane = defaultdict(list)

        for x, y in sortedKeys:
            yPlane[y].extend(plane[(x,y)])

        return list(yPlane.values())
        
        






        