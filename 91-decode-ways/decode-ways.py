class Solution:
    def numDecodings(self, s: str) -> int:
        return self._numDecodings(s, 0, {})
    
    def _numDecodings(self, s, i, memo):
        if i in memo:
            return memo[i]

        if i == len(s):
            return 1
        
        if s[i] == '0':
            return 0
        
        if s[i] == '1':
            out = []
            x = self._numDecodings(s, i + 1, memo)
            out.append(x)
            
            if i + 1 < len(s):
                y = self._numDecodings(s, i + 2, memo)
                out.append(y)
            
            memo[i] = sum(out)
            return memo[i]
        
        if s[i] == '2':
            out = []
            x = self._numDecodings(s, i + 1, memo)
            out.append(x)
            
            if i + 1 < len(s) and 0 <= int(s[i + 1]) <= 6:
                y = self._numDecodings(s, i + 2, memo)
                out.append(y)
            
            memo[i] =  sum(out)
            return memo[i]
        else:
            memo[i] =  self._numDecodings(s, i + 1, memo)
            return memo[i]

            