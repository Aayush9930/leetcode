class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x, y = 0, 0
        out = []

        while x < len(word1) and y < len(word2):
            out.append(word1[x])
            x += 1
            out.append(word2[y])
            y += 1

        while x < len(word1):
            out.append(word1[x])
            x += 1
        
        while y < len(word2):
            out.append(word2[y])
            y += 1
        
        return "".join(out)
