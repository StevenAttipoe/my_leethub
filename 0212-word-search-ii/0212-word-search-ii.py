class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEnd = True

class Solution:
    def __init__(self):
        self.trie = Trie()

    def buildTrie(self, words):
        for word in words:
            self.trie.insert(word)

    def search(self, r, c, board, res, trie, word):
        if trie.isEnd:
            res.append(''.join(word))
            trie.isEnd = False

        if r < 0 or r >= len(board):
            return

        if c < 0 or c >= len(board[0]):
            return

        if board[r][c] == '#' or board[r][c] not in trie.children:
            return

        char = board[r][c]
        board[r][c] = '#'
        nextLevel = trie.children[char]

        self.search(r + 1, c, board, res, nextLevel, word + [char])
        self.search(r - 1, c, board, res, nextLevel, word + [char])
        self.search(r, c + 1, board, res, nextLevel, word + [char])
        self.search(r, c - 1, board, res, nextLevel, word + [char])
        board[r][c] = char

        if len(nextLevel.children) == 0:
            del trie.children[char]
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.buildTrie(words)

        ROW, COL = len(board), len(board[0])
        foundWords = []

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] in self.trie.root.children:
                    self.search(r, c, board, foundWords, self.trie.root, [])

        return foundWords


