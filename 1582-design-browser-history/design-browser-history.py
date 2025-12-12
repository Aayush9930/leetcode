class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
    
    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps != 0 and self.curr.prev != None:
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.val  

    def forward(self, steps: int) -> str:
        while steps != 0 and self.curr.next != None:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)