# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(N) time & space
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return

            if node == p or node == q:
                return node
            
            leftMatch = dfs(node.left)
            rightMatch = dfs(node.right)

            if leftMatch and rightMatch:
                return node
                
            return leftMatch or rightMatch
        return dfs(root)

    # O(N) time & space
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return 0
            
            leftMatch = dfs(node.left)
            rightMatch = dfs(node.right)

            match = node == p or node == q

            if match + leftMatch + rightMatch == 2:
                self.lca = node
            
            return match or leftMatch or rightMatch

        dfs(root)
        return self.lca