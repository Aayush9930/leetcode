class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        longest = 0
        h = {}
        for r in range(len(s)):
            h[s[r]] = 1 + h.get(s[r], 0)
            if (r - l + 1) - max(h.values()) <= k:
                longest = max(longest, (r - l + 1))
            else:
                while (r - l + 1) - max(h.values()) > k:
                    h[s[l]] = h.get(s[l], 0) - 1
                    l += 1
        return longest 