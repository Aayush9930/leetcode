class OrderedStream:

    def __init__(self, n: int):
        self.lst = [ None ] * n
        self.visited = set()

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey - 1] = value
        out = []
        i = 0
        while i < len(self.lst) and self.lst[i] != None:
            if self.lst[i] not in self.visited:
                self.visited.add(self.lst[i])
                out.append(self.lst[i])
            i += 1
        return out

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)