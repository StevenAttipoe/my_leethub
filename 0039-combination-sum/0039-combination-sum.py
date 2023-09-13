class Solution:
    # Time Complexity: O(N^(T/M+1))
    # Space Complexity: O(T/M)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(list(comb))
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)
        return results

    # Time Complexity: O(M*M*N), N = len(candidates), M = target
    # Space Complexity: O(M*M)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates: # O(N): for each candidate
            for i in range(c, target+1): # O(M): for each possible value <= target
                if i == c: 
                    dp[i].append([c])
                for comb in dp[i-c]: 
                    dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]


        