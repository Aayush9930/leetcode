class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        not_seen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                if s[i] not in not_seen:  
                    not_seen[s[i]] = i
                else:
                    seen.add(s[i])
                    del not_seen[s[i]]
        
        if len(not_seen) == 0:
            return -1

        min_index = float('inf')
        for char in not_seen:
            if min_index > not_seen[char]:
                min_index = not_seen[char]
        
        return min_index
