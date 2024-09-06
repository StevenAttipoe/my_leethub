"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # O(N) time and O(1) space
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # Sandwich original and copied nodes
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        # Set random points for copied nodes
        cur = head
        while cur:
            copy = cur.next

            if cur.random:
                copy.random = cur.random.next
            else:
                copy.random = None

            cur = copy.next

        # Unweave original and copied nodes
        copiedHead = head.next
        originalHead = head
        result = head.next
        while originalHead:
            originalHead.next = originalHead.next.next

            if copiedHead.next:
                copiedHead.next = copiedHead.next.next
            else:
                copiedHead.next = None

            originalHead = originalHead.next
            copiedHead = copiedHead.next

        return result

    # O(N) time and space. Cleaner approach
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = { None : None }

        cur = head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copiedNode = hashmap[cur]

            copiedNode.next = hashmap[cur.next]
            copiedNode.random = hashmap[cur.random]

            cur = cur.next

        return hashmap[head]

    # O(N) time and space
    def copyRandomList3(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        copiedHead = Node(head.val)
        hashmap = {
            None : None,
            head : copiedHead
        }
        cur = copiedHead

        while head:
            if head.next in hashmap:
                cur.next = hashmap[head.next]
            else:
                copiedNext = Node(head.next.val)
                cur.next = copiedNext
                hashmap[head.next] = copiedNext

            if head.random in hashmap:
                cur.random = hashmap[head.random]
            else:
                copiedRandom = Node(head.random.val)
                cur.random = copiedRandom
                hashmap[head.random] = copiedRandom
            
            cur = cur.next
            head = head.next

        
        return copiedHead
        