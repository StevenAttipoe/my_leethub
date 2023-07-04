# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        stack = [[root, True]]
        result = []

        while stack:
            node, isDisjoint = stack.pop()
            if isDisjoint and node.val not in to_delete:
                result.append(node)

            if node.val in to_delete:
                isDisjoint = True
            else: 
                isDisjoint = False

            if node.right:
                stack.append([node.right, isDisjoint])
                if node.right.val in to_delete:
                    node.right = None

            if node.left:
                stack.append([node.left, isDisjoint])
                if node.left.val in to_delete:
                    node.left = None 
                
        return result


