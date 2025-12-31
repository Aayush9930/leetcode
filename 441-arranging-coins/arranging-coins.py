class Solution:
    def arrangeCoins(self, n: int) -> int:
        count_row = 0
        row_size = 1

        while n >= row_size:
            n = n - row_size
            count_row += 1
            row_size += 1
        
        return count_row
