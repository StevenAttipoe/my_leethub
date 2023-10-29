class Bucket:
    def __init__(self):
        self.bucket = []

    def put(self, key, value):
        for i, (k, _) in enumerate(self.bucket):
            if k == key:
                self.bucket[i] = (key, value)
                return
        self.bucket.append((key, value))
    
    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key):
        for i, (k, _) in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]

class MyHashMap:
    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].put(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].remove(key)

# class MyHashMap2:
#     def __init__(self):
#         self.data = [None] * 1000001        

#     def put(self, key: int, value: int) -> None:
#         self.data[key] = value        

#     def get(self, key: int) -> int:
#         val = self.data[key]
#         return val if val != None else -1

#     def remove(self, key: int) -> None:
#         self.data[key] = None

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)