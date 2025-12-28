class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self._generateParenthesis(n, n)
    
    def _generateParenthesis(self, left, right):
        if left == 0 and right == 0:
            return ['']

        out = []
        if left > 0:
            x = self._generateParenthesis(left - 1, right)
            for p in x:
                out.append("(" + p)
        
        if right > left:
            y = self._generateParenthesis(left, right - 1)
            for p in y:
                out.append(')' + p)
        
        return out
                

