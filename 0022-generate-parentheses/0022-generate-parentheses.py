class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(string_arr, open_count, close_count):
            if len(string_arr) == 2 * n:
                result.append("".join(string_arr))
                return
            
            if open_count < n:
                string_arr.append("(")
                backtrack(string_arr, open_count + 1, close_count)
                string_arr.pop()
            
            if close_count < open_count:
                string_arr.append(")")
                backtrack(string_arr, open_count, close_count + 1)
                string_arr.pop()
        
        backtrack([], 0, 0)
        return result

            

        
        