# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def helper(node):
            if not node:
                return []
            
            helper(node.left)
            nodes.append(node)
            helper(node.right)

        helper(root)
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = nodes[mid]
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(nodes) - 1)        