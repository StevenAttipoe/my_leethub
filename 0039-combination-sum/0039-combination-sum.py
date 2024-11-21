class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(s, comb):
            if sum(comb) == target:
                result.append(comb[:])
                return

            if s >= len(candidates) or sum(comb) > target:
                return

            comb.append(candidates[s])
            backtrack(s, comb)
            comb.pop()
            backtrack(s + 1, comb)

        backtrack(0, [])
        return result
        
        
        