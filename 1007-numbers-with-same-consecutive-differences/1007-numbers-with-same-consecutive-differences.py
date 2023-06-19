class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]

        queue = [i for i in range(1, 10)]
        
        for level in range(n - 1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                next_digit = set([tail_digit + k, tail_digit - k])

                for digit in next_digit:
                    if 0 <= digit < 10:
                        new_number = num * 10 + digit
                        next_queue.append(new_number)
            queue = next_queue
        return queue


        

