class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        visited = [math.inf] * n
        visited[src] = 0

        for _from,to,price in flights:
            adj[_from].append((to, price))

        queue = deque([(src, 0)])
        k += 1

        while k > 0 and queue:
            size = len(queue)
            while size > 0:
                cur_node, cur_price = queue.popleft()
                for neighbour, price in adj[cur_node]:
                    new_price = cur_price + price
                    if new_price < visited[neighbour]:
                        visited[neighbour] = new_price
                        queue.append((neighbour, new_price))
                size -= 1
            k -= 1
        
        return visited[dst] if visited[dst] != math.inf else -1
        