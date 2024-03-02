# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(H) time and space
    # O(H) = O(logN) for balanced trees
    
    def findSuccessor(self, root) -> int:
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def findPredecessor(self, root) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not (root.left or root.right):
                root = None

            elif root.right:
                root.val = self.findSuccessor(root)
                root.right = self.deleteNode(root.right, root.val)

            else:
                root.val = self.findPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
