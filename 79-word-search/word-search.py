class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.explore(board, word, (i, j), set()) == True:
                        return True

        return False 

    
    def explore(self, board, word, start, visited):
        x, y = start 
        if word == '':
            return True

        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return False 

        if (x, y) in visited or board[x][y] != word[0]:
            return False
        
        visited.add((x, y))

        found = self.explore(board, word[1:], (x + 1, y), visited) or self.explore(board, word[1:], (x - 1, y), visited) or self.explore(board, word[1:], (x, y + 1), visited) or self.explore(board, word[1:], (x, y - 1), visited)

        visited.remove((x, y))

        return found