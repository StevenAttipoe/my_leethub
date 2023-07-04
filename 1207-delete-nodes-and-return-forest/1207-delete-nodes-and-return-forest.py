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
            print(node.val, isDisjoint)
            if isDisjoint and node.val not in to_delete:
                result.append(node)

            if node.val in to_delete:
                isDisjoint = True
            else: isDisjoint = False

            if node.right:
                stack.append([node.right, isDisjoint])
                if node.right.val in to_delete:
                    # stack[-1][1] = True
                    # print(stack[-1][1])
                    node.right = None
                # else:
                #     if isDisjoint:
                #         result.append(node.right)

            if node.left:
                stack.append([node.left, isDisjoint])
                if node.left.val in to_delete:
                    # stack[-1][1] = True
                    node.left = None 
                # else:
                #     if isDisjoint:
                #         result.append(node.left)

        return result


