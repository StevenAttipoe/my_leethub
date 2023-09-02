# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 0

        self.count = 0 
        def postOrderTraverse(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left = postOrderTraverse(node.left)
            right = postOrderTraverse(node.right) 

            self.checkForGoodPairs(left, right, distance)
            pairs = left + right
            for i in range(len(pairs)):
                pairs[i] += 1 #Update pairs distance

            return pairs
        
        postOrderTraverse(root)
        return self.count

    def checkForGoodPairs(self,left, right, distance):
        for l in left:
            for r in right:
                if l + r <= distance:
                    self.count += 1