# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root

        stack = [root]
        while stack:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
                node.right = node.left
                node.left = None
            else:
                if stack:
                    node.right = stack[-1]
        