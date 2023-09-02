# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        q = deque()
        q.append(root)
        res = []
        isFlipped = False

        while q:
            n = len(q)
            level = deque()

            for _ in range(n):
                node = q.popleft()
                if isFlipped:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            isFlipped = not isFlipped
            res.append(level)

        return res

    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        q = deque()
        q.append(root)
        res = []
        isFlipped = False

        while q:
            n = len(q)
            level = []

            for _ in range(n):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if isFlipped:
                res.append(level[::-1])
            else:
                res.append(level)

            isFlipped = not isFlipped

        return res

        

        