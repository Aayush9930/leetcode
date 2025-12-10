from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0 
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))

        minutes = 0
        seen = 0   
        visited = set()

        while q:
            x, y, l = q.popleft()

            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                continue
            
            if grid[x][y] == 0 or (x, y) in visited:
                continue
            
            if grid[x][y] == 1:
                minutes = l
                seen += 1

            visited.add((x, y))

            q.append((x + 1, y, l + 1))
            q.append((x - 1, y, l + 1))
            q.append((x, y + 1, l + 1))
            q.append((x, y - 1, l + 1))

        if seen == count:
            return minutes
        return -1