class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = None
        actual_sum = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in seen:
                    a = grid[i][j]
                seen.add(grid[i][j])
                actual_sum += grid[i][j]

        n = len(grid)
        expected_sum = int((n**2) * ((n**2) + 1) / 2)


        b = expected_sum - (actual_sum - a)

        return [a, b]

