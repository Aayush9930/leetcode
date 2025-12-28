class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        out = []

        while l <= r and t <= b:
            # top row
            for c in range(l, r + 1):
                out.append(matrix[t][c])
            t += 1

            # right col 
            for row in range(t, b + 1):
                out.append(matrix[row][r])
            r -= 1
            
            if l > r or t > b:
                break
            
            # bottom row
            for c in range(r, l - 1, -1):
                out.append(matrix[b][c])
            b -= 1
            
            # left col
            for row in range(b, t - 1, -1):
                out.append(matrix[row][l])
            l += 1
            
           

        return out


