class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x = 0
        y = len(grid[0]) - 1
        count = 0

        while ( 0 <= x < len(grid) and 0 <= y < len(grid[0]) ):
            if grid[x][y] >= 0:
                x += 1

            elif grid[x][y] < 0:
                count += (len(grid) - x)
                y -= 1



        return count    

                