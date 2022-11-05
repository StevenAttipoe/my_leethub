# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        
        queue = [(root,"")]
        
        while queue:
            node, path = queue.pop(0)
            
            if not node.left and not node.right:
                output.append((path)+str(node.val))
                
            if node.left:
                queue.append((node.left, path + str(node.val)+"->"))
                
            if node.right:
                queue.append((node.right, path + str(node.val)+"->"))
                
        return output
            
            
        