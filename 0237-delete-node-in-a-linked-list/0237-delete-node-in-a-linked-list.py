# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(1) time and space
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next

    # O(n) time and O(1) space
    def deleteNode2(self, node):
        while node and node.next:
            next = node.next

            if not next.next:
                node.val = next.val
                node.next = None
                return

            node.val = next.val
            node = next

        