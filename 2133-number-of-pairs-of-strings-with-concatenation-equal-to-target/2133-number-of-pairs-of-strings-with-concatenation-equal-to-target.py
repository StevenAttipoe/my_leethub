class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = Counter(nums)
        pairs = 0

        for num, freq in count.items():
            if target.startswith(num):
                suffix = target[len(num):]
                pairs += freq * count[suffix]

                if num == suffix:
                    pairs -= count[suffix]

        return pairs