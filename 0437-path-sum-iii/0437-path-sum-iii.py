# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    paths = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, isRoot, runningSum):
            if not node:
                return

            runningSum -= node.val
            if runningSum == 0:
                self.paths += 1

            dfs(node.left, False, runningSum)
            dfs(node.right, False, runningSum)

            if isRoot:
                dfs(node.left, True, targetSum)
                dfs(node.right, True, targetSum)

        dfs(root, True, targetSum)
        return self.paths




    


        