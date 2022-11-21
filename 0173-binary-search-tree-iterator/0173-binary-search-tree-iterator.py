# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        def inOrderTraversal(root):
            if root:
                inOrderTraversal(root.right)
                self.stack.append(root.val)
                inOrderTraversal(root.left)
        inOrderTraversal(root)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()