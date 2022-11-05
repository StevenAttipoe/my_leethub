# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        stack = [(root, targetSum-root.val, [root.val])]
        
        while stack:
            node, diff, path = stack.pop()
            print(diff, path)
            
            if not node.right and not node.left and diff == 0:
                output.append(path)
                
            if node.right:
                stack.append((node.right, diff-node.right.val, path+[node.right.val]))
                
            if node.left:
                stack.append((node.left, diff-node.left.val, path+[node.left.val]))
                
        return output
        
        