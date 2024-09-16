class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        root = self.root

        for c in word:
            if c in root.children:
                root = root.children[c]     
            else:
                root.children[c] = TrieNode()
                root = root.children[c]

        root.isEnd = True
        

    def search(self, word: str) -> bool:
        root = self.root

        for c in word:
            if c in root.children:
                root = root.children[c]
            else:
                return False
        return root.isEnd

    def startsWith(self, prefix: str) -> bool:
        root = self.root

        for c in prefix:
            if c in root.children:
                root = root.children[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)