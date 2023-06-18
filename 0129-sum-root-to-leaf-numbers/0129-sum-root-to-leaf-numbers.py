# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        values = []

        while stack:
            node, number = stack.pop()
            number = number * 10 + node.val

            if node.right:
                stack.append((node.right, number))

            if node.left:
                stack.append((node.left, number))

            if not node.right and not node.left:
                values.append(number)

        return sum(values)
