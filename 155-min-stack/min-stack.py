class MinStack:

    def __init__(self):
        self.stk = []
        self.minLst = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minLst == []:
            self.minLst.append(val)
        else:
            m = min(self.minLst[-1], val)
            self.minLst.append(m)

    def pop(self) -> None:
        self.minLst.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minLst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()