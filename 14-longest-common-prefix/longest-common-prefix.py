class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len = float('inf')
        shortest_word = None
        for word in strs:
            if len(word) < shortest_len:
                shortest_len = len(word)
                shortest_word = word
        
        res = ''
        for i in range(len(shortest_word)):
            for s in strs:
                if shortest_word[i] == s[i]:
                    continue
                else:
                    return res
            res += shortest_word[i]
        return res


        