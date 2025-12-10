class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len = 0
        max_str = "" 
        for i in range(len(s)):
            # odd len str
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > max_len:
                    max_len = (r - l + 1)
                    max_str = s[l : r + 1]
                r += 1
                l -= 1
            
            # even len str
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > max_len:
                    max_len = (r - l + 1)
                    max_str = s[l : r + 1]
                l -= 1
                r += 1

        return max_str  
