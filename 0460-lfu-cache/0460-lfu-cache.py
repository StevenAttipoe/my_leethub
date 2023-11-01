class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.length += 1

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.length -= 1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.frequencies = defaultdict(DLL)
        self.minf = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        freq, node = self.cache[key]
        self.cache[key] = (freq + 1, node)
        self.frequencies[freq].removeNode(node)
        self.frequencies[freq + 1].addToHead(node)
        if self.minf == freq and self.frequencies[freq].length == 0:
            self.minf += 1
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity < 1:
            return

        if key in self.cache:
            freq, node = self.cache[key]
            node.key, node.value = key, value
            self.cache[key] = (freq, node)
            self.get(key)
        else:
            if len(self.cache) >= self.capacity:
                dll = self.frequencies[self.minf]
                del self.cache[dll.tail.prev.key]
                dll.removeNode(dll.tail.prev)

            newNode = Node(key, value)
            self.cache[key] = (1, newNode)
            self.frequencies[1].addToHead(newNode)
            self.minf = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)