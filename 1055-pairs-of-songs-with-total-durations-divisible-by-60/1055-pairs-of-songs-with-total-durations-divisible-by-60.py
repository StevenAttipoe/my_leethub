class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        noOfPairs = 0
        count = [0] * 60
        
        for duration in time:
            remainder, complement = duration % 60, -duration % 60
            
            noOfPairs += count[complement]
            count[remainder] += 1

        return noOfPairs