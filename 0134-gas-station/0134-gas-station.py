class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)

        if totalCost > totalGas:
            return -1

        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start = i + 1
        
        return start


    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)

        if totalCost > totalGas:
            return -1

        n = len(gas)

        for i in range(n):
            if gas[i] < cost[i]:
                continue
            
            cur = 0
            j = i

            while cur >= 0:
                cur += gas[j % n]
                cur -= cost[j % n]

                if cur < 0:
                    break

                j += 1

                if j % n == i:
                    return i
        
        return -1





        