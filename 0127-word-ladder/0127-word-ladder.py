class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)

        visit = set([beginWord])
        queue = deque([beginWord])
        step = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return step
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neighbour in graph[pattern]:
                        if neighbour not in visit:
                            visit.add(neighbour)
                            queue.append(neighbour)
            step += 1                
        return 0





