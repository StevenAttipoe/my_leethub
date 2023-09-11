# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        dummy = head
        while dummy:
            nodes.append(dummy)
            dummy = dummy.next

        n = len(nodes) if len(nodes) % 2 == 0 else len(nodes) + 1
        i = 0
        prev = None
        while i < (n // 2):
            if prev: #prev != None
                prev.next = nodes[i]

            nodes[i].next = nodes[-1 - i]
            prev = nodes[-1 - i]
            i += 1

        prev.next = None
            

























    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     if not head.next:
    #         return

    #     #Find middle
    #     slow = fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next

    #     #Reverse second half
    #     prev, cur = None, slow
    #     while cur:
    #         cur.next, prev, cur = prev, cur, cur.next

    #     #Merged first and second halves by order
    #     first = head
    #     second = prev
    #     while second.next:
    #         first.next, first = second, first.next
    #         second.next, second = first, second.next

    # def reorderList2(self, head: Optional[ListNode]) -> None:
    #     if not head.next:
    #         return

    #     dummy = head
    #     nodes = []
    #     while dummy:
    #         nodes.append(dummy)
    #         dummy = dummy.next

    #     prev = None
    #     n = len(nodes) if len(nodes) % 2 == 0 else len(nodes) + 1
    #     r = 0
    #     for i in range(n // 2):
    #         cur = nodes[i]
    #         end = nodes[-1 + r]
    #         nxt = cur.next
    #         cur.next = end
    #         end.next = nxt
    #         r -= 1

    #     end.next = None





        





        