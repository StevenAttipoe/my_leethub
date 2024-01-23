# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def recurseTree(node):
            if node:
                nonlocal rangeSum

                if low <= node.val <= high:
                    rangeSum += node.val

                recurseTree(node.left)
                recurseTree(node.right)

        rangeSum = 0
        recurseTree(root) 
        return rangeSum

    def rangeSumBST2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangeSum = [0]

        def recurseTree(node):
            if not node:
                return

            if low <= node.val <= high:
                rangeSum[0] += node.val

            recurseTree(node.left)
            recurseTree(node.right)

        recurseTree(root) 
        return rangeSum[0]