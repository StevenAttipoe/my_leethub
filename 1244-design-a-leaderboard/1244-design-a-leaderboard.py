class Leaderboard:
    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            oldScore = self.scores[playerId]

            n = self.sortedScores[-oldScore]
            if n == 1:
                del self.sortedScores[-oldScore]
            else:
                self.sortedScores[-oldScore] -= 1

            newScore = oldScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1

        else:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1

    def top(self, K: int) -> int:
        topK = count = 0

        for score in self.sortedScores.keys():
            for i in range(self.sortedScores[score]):
                topK += abs(score)
                count += 1

                if count == K:
                    break
            if count == K:
                    break
        return topK


    def reset(self, playerId: int) -> None:
        oldScore = self.scores[playerId]
        n = self.sortedScores[-oldScore]
        if n == 1:
            del self.sortedScores[-oldScore]
        else:
            self.sortedScores[-oldScore] -= 1
        del self.scores[playerId]

class Leaderboard2:
    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for score in self.scores.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0

class Leaderboard3:
    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        sortedScores = sorted(self.scores.values(), key = lambda x: -x)
        topK = 0
        for i in range(K):
            topK += sortedScores[i]
        return topK

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)