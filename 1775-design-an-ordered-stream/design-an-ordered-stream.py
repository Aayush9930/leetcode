class OrderedStream:

    def __init__(self, n: int):
        self.l = [0] * n
        self.visited = set()

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey - 1] = value
        out = []
        i = 0 
        while i < len(self.l) and self.l[i] != 0:
            if self.l[i] not in self.visited:
                out.append(self.l[i])
                self.visited.add(self.l[i])
            i += 1
        return out
            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)