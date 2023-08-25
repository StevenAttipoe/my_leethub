class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        ''' 
        The smallest possible difference is given as
        =>  (max(A) - K) - (min(A) + K) 
            = max(A) - K - min(A) - K
        '''
        
        largest_min = min(nums) + k
        smallest_max = max(nums) - k

        return max(0, max(nums) - min(nums) - k - k)

