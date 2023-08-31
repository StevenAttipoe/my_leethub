class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        cost = 0

        for status in customers:
            if status == 'Y':
                cost += 1

        costs = {0 : cost}

        for i in range(1, n + 1):
            if customers[i - 1] == 'Y':
                costs[i] = costs[i - 1] - 1
            else:
                costs[i] = costs[i - 1] + 1

        minPenalty = min(costs.values())
        bestTime =[ key for key in costs.keys() if minPenalty == costs[key]]
        return bestTime[0]

