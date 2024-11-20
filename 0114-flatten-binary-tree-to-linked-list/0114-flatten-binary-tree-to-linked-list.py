# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

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

    def flatten2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if not node:
                return node

            dfs(node.right)
            dfs(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node
        
        dfs(root)



        
