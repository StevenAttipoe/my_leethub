# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        def dfs(node, isStart, pathSum) -> bool:
            if not node:
                return
            
            totalSum = pathSum + node.val
            if totalSum == targetSum:
                self.count += 1
                
            dfs(node.left, False, totalSum)
            dfs(node.right, False, totalSum)

            if isStart:
                dfs(node.left, True, 0)
                dfs(node.right, True, 0)

        dfs(root, True, 0)
        return self.count