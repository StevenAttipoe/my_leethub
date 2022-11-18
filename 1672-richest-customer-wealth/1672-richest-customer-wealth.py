class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for  i in range(len(accounts)):
            currWeath = 0
            
            for j in range(len(accounts[0])):
                currWeath += accounts[i][j]
                
            maxWealth = max(maxWealth, currWeath)
            
        return maxWealth
        