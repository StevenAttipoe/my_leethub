class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)

        for p, pp in zip(pid, ppid):
            graph[pp].append(p)

        result = []
        queue = deque([kill])

        while queue:
            p = queue.popleft()

            result.append(p)

            for child in graph[p]:
                queue.append(child)
            
        return result


        