# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node:
                return True
            
            if not inorder(node.left):
                return False
            
            if node.val <= self.prev:
                return False

            self.prev = node.val
            return inorder(node.right)

        self.prev = -math.inf
        return inorder(root)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, low, high):
            if not node:
                return True

            if low >= node.val or high <= node.val:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high) 
        
        return dfs(root, -math.inf, math.inf)       