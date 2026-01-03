class Solution:
    def longestBalanced(self, s: str) -> int:
        m = 0
        for i in range(len(s)):
            f = {}
            for j in range(i, len(s)):
                f[s[j]] = 1 + f.get(s[j], 0)
                if len(set(f.values())) == 1:
                    m = max(m, j - i + 1)
        return m