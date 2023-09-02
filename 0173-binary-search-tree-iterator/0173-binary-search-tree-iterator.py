# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inOrderTravere(node, stack):
            if not node:
                return
            inOrderTravere(node.left, stack)
            stack.append(node.val)
            inOrderTravere(node.right, stack)

        self.stack = []
        inOrderTravere(root, self.stack)
        self.index = 0        

    def next(self) -> int:
        val = self.stack[self.index]
        self.index += 1
        return val
        

    def hasNext(self) -> bool:
        return self.index < len(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()