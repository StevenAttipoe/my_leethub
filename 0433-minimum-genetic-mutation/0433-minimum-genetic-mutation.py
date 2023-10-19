class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        seen = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            for c in 'ACGT':
                for i in range(len(gene)):
                    neighbour = gene[:i] + c + gene[i + 1:]
                    if neighbour not in seen and neighbour in bank:
                        queue.append((neighbour, steps + 1))
                        seen.add(neighbour)
        return - 1



