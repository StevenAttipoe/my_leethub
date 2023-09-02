# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, order):
            if not root:
                return

            helper(root.left, order)
            helper(root.right, order)
            order.append(root.val)
        
        res = []
        helper(root, res)
        print(res)
        return res