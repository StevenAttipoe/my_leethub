class Node:
    def __init__(self, key = 0, val = 0):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        self.size = 0
        self.nodes = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.nodes.get(key, None)

        if not node:
            return -1
        
        self.removeNode(node)
        self.addToHead(node)
    
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.removeNode(node)
            self.addToHead(node)

        else:
            if self.size >= self.capacity:
                lru = self.tail.prev
                self.removeNode(lru)
                del self.nodes[lru.key]
                node = Node(key, value)
                self.nodes[key] = node
                self.addToHead(node)

            else:
                node = Node(key, value)
                self.addToHead(node)
                self.nodes[key] = node
                self.size += 1

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)