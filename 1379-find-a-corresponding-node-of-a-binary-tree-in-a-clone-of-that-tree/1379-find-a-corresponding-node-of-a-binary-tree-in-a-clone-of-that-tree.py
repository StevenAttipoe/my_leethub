# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(originalNode, clonedNode):
            nonlocal res
            if not originalNode or res:
                return

            if originalNode == target:
                res = clonedNode
                return

            dfs(originalNode.left, clonedNode.left)
            dfs(originalNode.right, clonedNode.right)

        res = None
        dfs(original, cloned)
        return res
        