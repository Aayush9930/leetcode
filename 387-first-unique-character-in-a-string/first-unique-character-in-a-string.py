class Solution:
    def firstUniqChar(self, s: str) -> int:
        countC = defaultdict(int)
        for c in s:
            countC[c] += 1
        for i in range(len(s)):
            if countC[s[i]] == 1:
                return i
        return -1


