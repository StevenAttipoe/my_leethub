# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node): #O(n)
            if not node:
                return [True, 0] 

            left = helper(node.left)
            right = helper(node.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return helper(root)[0]

    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if not root:
                return -1
            return 1 + max(getHeight(root.left), getHeight(root.right))

        def helper(node): #O(n * h) or O(n * logn)
            if not node:
                return True
            
            #check if node is balanced and check for subtrees
            res = abs(getHeight(node.left) - getHeight(node.right)) < 2 \
                and helper(node.left) \
                and helper(node.right)
            
            return res

        return helper(root)

        