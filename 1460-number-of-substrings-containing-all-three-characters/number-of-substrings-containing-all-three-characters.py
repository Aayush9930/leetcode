class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        h = {}
        l = 0
        res = 0

        for r in range(len(s)):
            # increase the window 
            h[s[r]] = 1 + h.get(s[r], 0)

            # while valid count the result
            if len(h) == 3:
                while h[s[l]] > 1:
                    h[s[l]] -= 1
                    l += 1
                res += l + 1

        return res