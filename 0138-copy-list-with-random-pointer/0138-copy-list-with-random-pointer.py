"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
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
                if hashmap[head.random]:
                    print(cur.val, hashmap[head.random].val)
            else:
                print(cur.val, "here")
                copiedRandom = Node(head.random.val)
                cur.random = copiedRandom
                hashmap[head.random] = copiedRandom
            
            cur = cur.next
            head = head.next

        
        return copiedHead
        