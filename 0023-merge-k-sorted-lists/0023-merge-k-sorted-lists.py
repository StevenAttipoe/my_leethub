# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = cur = ListNode(0)
        heap = []

        for i in range(len(lists)):
            list_head = lists[i]
            if list_head:
                heapq.heappush(heap, (list_head.val, i, lists[i]))

        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next



