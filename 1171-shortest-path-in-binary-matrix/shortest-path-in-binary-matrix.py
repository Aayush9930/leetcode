
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque([(0, 0, 1)])

        while q:
            x, y, l = q.popleft()

            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                continue

            if grid[x][y] != 0 or (x, y) in visited:
                continue

            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return l

            visited.add((x, y)) 

            q.append((x + 1, y, l + 1))
            q.append((x - 1, y, l + 1))
            q.append((x, y + 1, l + 1))
            q.append((x, y - 1, l + 1))
            q.append((x + 1, y + 1, l + 1))
            q.append((x - 1, y + 1, l + 1))
            q.append((x + 1, y - 1, l + 1))
            q.append((x - 1, y - 1, l + 1))
        return -1
























    #     x = self._shortestPathBinaryMatrix(grid, (0, 0), set(), {})

    #     if x == float('inf'):
    #         return -1
        
    #     return x
    

    # def _shortestPathBinaryMatrix(self, grid, start, visited, memo):
    #     if (start, tuple(visited)) in memo:
    #         return memo[(start, tuple(visited))]
    #     x, y = start

    #     if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
    #         return float('inf')

    #     if (x, y) in visited:
    #         return float('inf')

    #     if grid[x][y] != 0:
    #         return float('inf')
        

    #     if x == len(grid) - 1 and y == len(grid[0]) - 1:
    #         return 1

    #     visited.add((x, y))

    #     found =  1 + min(
    #         self._shortestPathBinaryMatrix(grid, (x + 1, y), visited, memo), 
    #         self._shortestPathBinaryMatrix(grid, (x - 1, y), visited, memo), 
    #         self._shortestPathBinaryMatrix(grid, (x, y + 1), visited, memo), 
    #         self._shortestPathBinaryMatrix(grid, (x, y - 1), visited, memo),  
    #         self._shortestPathBinaryMatrix(grid, (x - 1, y + 1), visited, memo), 
    #         self._shortestPathBinaryMatrix(grid, (x + 1, y + 1), visited, memo), 
    #         self._shortestPathBinaryMatrix(grid, (x - 1, y - 1), visited, memo), 
    #         self._shortestPathBinaryMatrix(grid, (x + 1, y - 1), visited, memo)
    #     )

    #     visited.remove((x, y))

    #     memo[(start, tuple(visited))] =  found
    #     return memo[(start, tuple(visited))]
