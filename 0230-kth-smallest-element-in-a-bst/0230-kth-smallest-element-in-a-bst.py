# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.smallestKValue = root.val

        def dfs(node):
            if not node:
                return None

            dfs(node.left)


            dfs(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def dfs(node):
            if not node:
                return None

            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        vals.sort()
        return vals[k - 1]



        