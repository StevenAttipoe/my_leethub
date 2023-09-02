# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
            
        def helper(node, values):
            if not node:
                return
            values.append(node.val)
            helper(node.left, values)
            helper(node.right, values)

        values = []
        helper(root, values)
        return values