# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N) time and space
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        def buildBST(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(vals[mid])

            if l == r:
                return root

            root.left = buildBST(l, mid - 1)
            root.right = buildBST(mid + 1, r)

            return root

        return buildBST(0, len(vals) - 1)


    
    # O(NlogN) time
    # O(logN) space
    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        mid, prev = self.findPivot(head)
        root = TreeNode(mid.val)

        if prev:
            prev.next = None
        else:
            head = None

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

    def findPivot(self, head):
        prev = None
        slow = head
        fast = head.next

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return slow, prev


        
        