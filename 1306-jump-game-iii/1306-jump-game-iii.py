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


    def canReach2(self, arr: List[int], start: int) -> bool:
        def dfs(cur):
            if 0 <= cur < len(arr) and arr[cur] >= 0:
                if arr[cur] == 0:
                    return True

                arr[cur] = -arr[cur]
                return dfs(cur + arr[cur]) or dfs(cur - arr[cur])

        return dfs(start)


        