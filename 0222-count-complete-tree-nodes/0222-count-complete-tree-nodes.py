# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getLeftDepth(node):
            if not node:
                return 0
            return 1 + getLeftDepth(node.left)
            
        def getRightDepth(node):
            if not node:
                return 0
            return 1 + getRightDepth(node.right)
        
        if not root:
            return 0
        
        leftDepth = getLeftDepth(root)
        rightDepth = getRightDepth(root)
        
        if leftDepth == rightDepth:
            return (2**leftDepth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

   

        
        