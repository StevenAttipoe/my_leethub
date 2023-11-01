class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)
        self.minf = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        freq, val = self.cache[key]
        del self.frequencies[freq][key]
        self.cache[key] = (freq + 1, val)
        self.frequencies[freq + 1][key] = True
        if self.minf == freq and not self.frequencies[self.minf]:
            self.minf += 1

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            freq, val = self.cache[key]
            self.cache[key] = (freq, value)
            self.get(key)
        else:
            if len(self.cache) >= self.capacity:
                k, _ = self.frequencies[self.minf].popitem(last= False)
                del self.cache[k]

            self.cache[key] = (1, value)
            self.frequencies[1][key] = True
            self.minf = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)