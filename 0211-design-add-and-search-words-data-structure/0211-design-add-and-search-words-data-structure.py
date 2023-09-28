class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd= True

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            if i == len(word):
                return cur.isEnd
            
            if word[i] == ".":
                for child in cur.children.keys():
                    if dfs(cur.children[child], i + 1):
                        return True

            else:
                if word[i] in cur.children:
                    return dfs(cur.children[word[i]], i + 1)
            
            return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)