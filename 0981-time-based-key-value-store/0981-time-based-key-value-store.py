class TimeMap:
    def __init__(self):
        self.keyTimeMap = {}

    """ 
        O(N * L) time and space
        N - number of calls
        L - time to hash string / length of the string to save
    """
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyTimeMap:
            self.keyTimeMap[key] = []

        self.keyTimeMap[key].append([timestamp, value])
        

    """
        O(N * logM * L) time
    """
    # O(T) time
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyTimeMap:
            return ""

        if timestamp < self.keyTimeMap[key][0][0]:
            return ""

        left, right = 0, len(self.keyTimeMap[key])
        while left < right:
            mid = (left + right) // 2

            if self.keyTimeMap[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        if right != 0:
            return self.keyTimeMap[key][right - 1][1]

        return ""

class TimeMap2:
    def __init__(self):
        self.keyTimeMap = {}


    """ 
        O(N * L) time and space
    """
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyTimeMap:
            self.keyTimeMap[key] = {}

        self.keyTimeMap[key][timestamp] = value
        

    """
        O(N * timestamp * L) time
    """
    # O(T) time
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyTimeMap:
            return ""

        for time in range(timestamp, 0, -1):
            if time in self.keyTimeMap[key]:
                return self.keyTimeMap[key][time]

        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)