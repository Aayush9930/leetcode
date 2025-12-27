class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self._uniquePathsWithObstacles(obstacleGrid, (0, 0), {})
    
    def _uniquePathsWithObstacles(self, grid, start, memo):
        x, y = start 

        if start in memo:
            return memo[start]

        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return 0 
        
        if grid[x][y] == 1:
            return 0 
        
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return 1
        
        memo[start] =  self._uniquePathsWithObstacles(grid, (x, y + 1), memo) + self._uniquePathsWithObstacles(grid, (x + 1, y), memo)

        return memo[start]

