class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            # the required row reached
            else:
                l, r = 0, len(matrix[0])
                while l <= r:
                    mid = (l+r)//2
                    if target > matrix[mid_row][mid]:
                        l = mid + 1
                    elif target < matrix[mid_row][mid]: 
                        r = mid - 1
                    else:
                        return True
                return False
        return False

