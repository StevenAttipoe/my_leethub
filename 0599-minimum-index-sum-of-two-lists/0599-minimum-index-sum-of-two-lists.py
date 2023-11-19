class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commonStrings, leastIndexSum, = deque(), math.inf
        list1Map = {}

        for i, string in enumerate(list1):
            list1Map[string] = i

        for i, string in enumerate(list2):
            if string in list1Map:
                indexSum = list1Map[string] + i

                if indexSum == leastIndexSum:
                    leastIndexSum = indexSum
                    commonStrings.append(string)

                elif indexSum < leastIndexSum:
                    leastIndexSum = indexSum
                    while commonStrings: 
                        commonStrings.popleft()
                    commonStrings.append(string)
        
        return commonStrings

        