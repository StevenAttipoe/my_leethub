class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.cur = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value

        result = []
        
        while self.cur < len(self.stream) and self.stream[self.cur] != None:
            result.append(self.stream[self.cur])
            self.cur += 1
        
        return result



        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)