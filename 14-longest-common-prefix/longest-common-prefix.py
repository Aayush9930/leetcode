class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        shortest = float('inf')
        shortest_word = None

        for s in strs:
            if len(s) < shortest:
                shortest = len(s)
                shortest_word = s


        for i in range(len(shortest_word)): 
            for word in strs:
                if word[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

