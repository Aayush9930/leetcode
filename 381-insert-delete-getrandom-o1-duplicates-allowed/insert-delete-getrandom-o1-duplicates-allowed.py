class RandomizedCollection:

    def __init__(self):
        self.h = defaultdict(set)
        self.lst = []

    def insert(self, val: int) -> bool:
        idx = len(self.lst)
        self.lst.append(val)
        self.h[val].add(idx)

        if len(self.h[val]) == 1:
            return True
        return False

    def remove(self, val: int) -> bool:
        if len(self.h[val]) == 0:
            return False
        
        idx = self.h[val].pop()
        if idx == len(self.lst) - 1:
            self.lst.pop()
            return True




        self.lst[idx] = self.lst[-1]
        self.h[self.lst[-1]].remove(len(self.lst) - 1)
        self.h[self.lst[-1]].add(idx)
        self.lst.pop()

        return True

    def getRandom(self) -> int:
        idx = random.randrange(len(self.lst))
        return self.lst[idx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()