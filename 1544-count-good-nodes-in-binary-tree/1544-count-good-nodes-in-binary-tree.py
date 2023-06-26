# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def preOrderTraversal(root, prev):
            if not root:
                return 0

            numOfGoodNode = 0

            if root.val >= prev:
                numOfGoodNode = 1

            numOfGoodNode += preOrderTraversal(root.left, max(root.val, prev))
            numOfGoodNode += preOrderTraversal(root.right, max(root.val, prev))

            return numOfGoodNode

        return preOrderTraversal(root, -10000)
        