class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        queue = deque([start])

        while queue:
            index = queue.popleft()

            if arr[index] == 0:
                return True

            if arr[index] < 0:
                continue

            for jump in [index + arr[index], index - arr[index]]:
                if 0 <= jump < N:
                    queue.append(jump)

            arr[index] = -arr[index]

        return False



        