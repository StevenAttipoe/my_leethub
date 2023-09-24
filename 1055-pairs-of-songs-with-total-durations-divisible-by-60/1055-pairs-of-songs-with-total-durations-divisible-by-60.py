class Solution:
    def numPairsDivisibleBy60III(self, time: List[int]) -> int:
        noOfPairs = 0
        count = [0] * 60
        
        for duration in time:
            remainder, complement = duration % 60, -duration % 60
            print(remainder, complement)
            noOfPairs += count[complement]
            count[remainder] += 1

        return noOfPairs

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        noOfPairs = 0
        count = {}
        
        for duration in time:
            remainder, complement = duration % 60, (60-duration) % 60
            if complement in count:
                noOfPairs += count[complement]
            count[remainder] = count.get(remainder, 0) + 1

        return noOfPairs

    def numPairsDivisibleBy60II(self, time: List[int]) -> int:
        noOfPairs = 0
        
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    noOfPairs += 1

        return noOfPairs