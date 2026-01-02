class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [ [0] * 26 for _ in range(rows) ]
        
    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord("A") # 0 -> 25 
        row = int(cell[1:]) - 1
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord("A") # 0 -> 25 
        row = int(cell[1:]) - 1
        self.grid[row][col] = 0

    def synth(self, s):
        if s[0].isdigit():
            return int(s)
        col = ord(s[0]) - ord("A") # 0 -> 25 
        row = int(s[1:]) - 1
        return self.grid[row][col]


    def getValue(self, formula: str) -> int:
        a = formula[1:].split('+')
        val1 = self.synth(a[0])
        val2 = self.synth(a[1])
        return val1 + val2




# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)