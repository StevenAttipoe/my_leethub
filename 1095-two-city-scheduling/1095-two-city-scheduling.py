class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        
        totalCost = 0
        n = len(costs) // 2
        
        for i in range(n):
            totalCost += costs[i][0] + costs[i + n][1]
            
        return totalCost
         