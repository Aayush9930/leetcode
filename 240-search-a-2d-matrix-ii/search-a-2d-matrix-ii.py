class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = 0
        y = len(matrix[0]) - 1 
    
        while (0 <= x < len(matrix) and 0 <= y < len(matrix[0])):
            if matrix[x][y] > target:
                y = y - 1

            elif matrix[x][y] < target:
                x = x + 1

            else:
                return True

        return False 
 
        