class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        def explore(start):
            x, y = start
            # check if the coordinate is in bounds -> return if out
            if not (0 <= x < rows and 0 <= y < cols):
                return
            # if the it is water or if in visited -> return
            if grid[x][y] == '0' or (x, y) in visited:
                return

            # add the coordinate into visited 
            visited.add((x,y))
            # iterate top, down, left, right
            #top
            explore((x - 1, y))
            #bottom
            explore((x + 1, y))
            #left
            explore((x, y - 1))
            #right
            explore((x, y + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    explore((i, j))
                    count += 1


        return count



                