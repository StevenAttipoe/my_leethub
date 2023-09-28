class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return cur.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        lastChar = ''

        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
                lastChar = char
            else:
                return False
        return prefix[-1] == lastChar
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)