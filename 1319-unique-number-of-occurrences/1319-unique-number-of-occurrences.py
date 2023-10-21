class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        uniqueSet = set()

        for num in arr:
            count[num] = count.get(num, 0) + 1

        for occurance in count.values():
            if occurance in uniqueSet:
                return False
            uniqueSet.add(occurance)
            
        return True

                