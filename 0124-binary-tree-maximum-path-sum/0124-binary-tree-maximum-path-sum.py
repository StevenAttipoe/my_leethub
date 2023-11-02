# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float('-inf')
        self.helper(root)
        return self.maxPathSum

    def helper(self, node):
        if not node:
            return 0
        
        leftPathSum = self.helper(node.left)
        rightPathSum = self.helper(node.right)

        self.maxPathSum = max(self.maxPathSum, node.val + leftPathSum + rightPathSum)
        
        return max(0, node.val + max(leftPathSum, rightPathSum))