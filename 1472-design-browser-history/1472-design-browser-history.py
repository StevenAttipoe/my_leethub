class BrowserHistory:
    class Node:
        def __init__(self, val): 
            self.val = val
            self.prev = None
            self.next = None
            
    def __init__(self, homepage: str):
        self.history = BrowserHistory.Node(homepage)

    def visit(self, url: str) -> None:
        node = BrowserHistory.Node(url)
        node.prev = self.history
        self.history.next = node
        self.history = self.history.next
          

    def back(self, steps: int) -> str:
        while self.history.prev and steps:
            self.history = self.history.prev
            steps -= 1
        return self.history.val
            
    def forward(self, steps: int) -> str:
        while self.history.next and steps:
            self.history = self.history.next
            steps -= 1
        return self.history.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)