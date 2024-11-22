# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(node, path, pathSum):
            if not node:
                return
            
            pathSum += node.val
            path.append(node.val)

            if (not node.left and not node.right) and pathSum == targetSum:
                paths.append(path[:])
                path.pop()
                return

            dfs(node.left, path, pathSum)
            dfs(node.right, path, pathSum)

            path.pop()
            
        
        dfs(root, [], 0)
        return paths

        