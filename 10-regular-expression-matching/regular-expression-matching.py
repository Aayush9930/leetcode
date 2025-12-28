class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self._isMatch(s, p, 0, 0, {})
    
    def _isMatch(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        
        if j + 1 < len(p) and p[j + 1] == "*":
            x = False
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                x = self._isMatch(s, p, i + 1, j, memo)

            y = self._isMatch(s, p, i, j + 2, memo)

            memo[(i, j)] =  x or y
            return memo[(i, j)]
        
        if i < len(s) and (s[i] == p[j] or p[j] == "."):
            memo[(i, j)] =  self._isMatch(s, p, i + 1, j + 1, memo)
            return memo[(i, j)]
        
        memo[(i, j)] = False
        return memo[(i, j)]
