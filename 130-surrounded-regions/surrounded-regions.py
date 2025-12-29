class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = set()
        for c in range(len(board[0])):
            if (0, c) not in visited and board[0][c] == "O":
                self.dfs(board, (0, c), visited)
        
        for c in range(len(board[0])):
            if (len(board) - 1, c) not in visited and board[len(board) - 1][c] == "O":
                self.dfs(board, (len(board) - 1, c), visited)
            
        for r in range(len(board)):
            if (r, 0) not in visited and board[r][0] == "O":
                self.dfs(board, (r, 0), visited)  

        for r in range(len(board)):
            if (r, len(board[0]) - 1) not in visited and board[r][len(board[0]) - 1] == "O":
                self.dfs(board, (r, len(board[0]) - 1), visited)  
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"
    
    def dfs(self, board, start, visited):
        x, y = start

        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return 
        
        if board[x][y] == "X" or (x, y) in visited:
            return 
        
        visited.add((x, y))

        self.dfs(board, (x + 1, y), visited)
        self.dfs(board, (x - 1, y), visited)
        self.dfs(board, (x, y + 1), visited)
        self.dfs(board, (x, y - 1), visited)

                 
        


