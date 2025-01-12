# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        columnTable = defaultdict(list)

        while queue:
            node, pos = queue.popleft()

            if node:
                columnTable[pos].append(node.val)
                
                queue.append((node.left, pos - 1))
                queue.append((node.right, pos + 1))
        
        return [columnTable[key] for key in sorted(columnTable.keys())]            

            
        
        