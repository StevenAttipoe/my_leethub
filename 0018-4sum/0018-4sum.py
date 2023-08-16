class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quads = set()
        sum_dic = defaultdict(dict)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                two_sum = nums[i] + nums[j]
                pair = tuple(sorted((nums[i], nums[j])))
                if pair in sum_dic[two_sum]:
                        sum_dic[two_sum][pair].append([i, j])
                else:
                    sum_dic[two_sum][pair] = [[i, j]]

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                for pair in sum_dic[complement]:
                    for k, l in sum_dic[complement][pair]:
                        if len(set((i,j,k,l)))==4:
                            quads.add(tuple(sorted((nums[i], nums[j], nums[k], nums[l]))))
                            break

        return quads



            
