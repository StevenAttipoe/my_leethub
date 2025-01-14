class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        costs.sort(key = lambda x: x[0] - x[1])
        minCost = 0

        for i in range(N):
            minCost += costs[i][0] + costs[i + N][1]
        
        return minCost
        