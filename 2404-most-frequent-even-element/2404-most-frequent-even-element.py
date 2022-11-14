class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count  = {}
        
        for num in nums:
            if num % 2 == 0:
                if num in count:
                    count[num] += 1
                else:  
                    count[num] = 1
                    
        freq = 0
        mostFreqEvenNum = -1
        for key in count.keys():
            if count[key] > freq:
                freq = count[key]
                mostFreqEvenNum = key
                
            if count[key] == freq:
                if key < mostFreqEvenNum:
                    mostFreqEvenNum = key
                    
        return mostFreqEvenNum
        