class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysToWait = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                curr = stack.pop()
                day = i - curr
                daysToWait[curr] = day
                
            stack.append(i)
            
        return daysToWait
                
            