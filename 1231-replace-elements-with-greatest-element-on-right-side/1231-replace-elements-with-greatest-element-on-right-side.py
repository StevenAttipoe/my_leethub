class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 
        n = len(arr)
        high = 0

        if n > 1:
            arr[0] = max(arr[1:])
            high = arr[0]

        for i in range(n - 1):
            if arr[i] != high:
                arr[i] = high
            else:
                high = max(arr[i+1:])
                arr[i] = high

        arr[-1] = -1

        return arr
