# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if not vals:
            return None

        def dfs(nums):
            val = nums.popleft()
            if not val:
                return None

            root = TreeNode(val)
            root.left = dfs(nums)
            root.right = dfs(nums)

            return root

        return dfs(deque(vals))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans