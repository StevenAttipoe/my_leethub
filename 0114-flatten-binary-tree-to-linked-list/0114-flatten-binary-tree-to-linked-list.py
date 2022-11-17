# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = [root]
        
        while stack and root:
            cur = stack.pop()
            
            if cur.right:
                stack.append(cur.right)
                
            if cur.left:
                stack.append(cur.left)
                cur.right = cur.left
                cur.left = None
            
            else:
                if stack:
                    cur.right = stack[-1]
                