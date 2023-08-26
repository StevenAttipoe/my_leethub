# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    paths = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curSumPath, cache):
            if not node:
                return

            curSumPath += node.val
            oldPathSum = curSumPath - targetSum

            self.paths += cache.get(oldPathSum, 0)
            cache[curSumPath] = cache.get(curSumPath, 0) + 1

            dfs(node.left, curSumPath, cache)
            dfs(node.right, curSumPath, cache)

            # when move to a different branch, the curSumPath is no longer available
            cache[curSumPath] -= 1

        cache = {0:1}
        dfs(root, 0, cache)
        return self.paths




    


        