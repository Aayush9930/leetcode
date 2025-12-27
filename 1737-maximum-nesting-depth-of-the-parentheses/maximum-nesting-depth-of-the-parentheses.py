class Solution:
    def maxDepth(self, s: str) -> int:
        stk = []
        max_depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                stk.append(s[i])
                max_depth = max(max_depth, len(stk))
            elif s[i] == ')':
                stk.pop()
        
        return max_depth