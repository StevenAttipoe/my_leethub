class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        t = self.root
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        
        t["-"] = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rowNum = len(board)
        colNum = len(board[0])
        result = []
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        def dfs(row, col, path, parent):
            nonlocal rowNum
            nonlocal colNum
            
            if '-' in parent:
                result.append(path)
                # avoid duplicate
                del parent['-']
            
            if row < 0 or row >= rowNum or col < 0 or col >= colNum:
                return
            
            char = board[row][col]
            
            if char == "#":
                return
            
            if char not in parent:
                return
            
            curNode = parent[char]
            
            # find the char, set to visited
            board[row][col] = "#"
            dfs(row+1, col, path + char, curNode)
            dfs(row-1, col, path + char, curNode)
            dfs(row, col+1, path + char, curNode)
            dfs(row, col-1, path + char, curNode)
            board[row][col] = char
            
            # optimization: remove the matched leaf node in Trie.
            if not curNode:
                parent.pop(char)
            
        
        for row in range(rowNum):
            for col in range(colNum):
				# optimiztation 
                if board[row][col] in trie.root:
                    dfs(row, col, "", trie.root)
        
        return result