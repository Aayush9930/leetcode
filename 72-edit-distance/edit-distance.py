class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self._minDistance(word1, word2, 0, 0, {})

    def _minDistance(self, word1, word2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= len(word1) and j >= len(word2):
            return 0
        
        if j >= len(word2):
            return len(word1) - i
        
        if i >= len(word1):
            return len(word2) - j
        
        if i < len(word1) and word1[i] == word2[j]:
            memo[(i, j)] = self._minDistance(word1, word2, i + 1, j + 1, memo)
            return memo[(i, j)]
        out = []
        # insert 
        insert = 1 + self._minDistance(word1, word2, i, j + 1, memo)
        out.append(insert)
        # delete 
        if i < len(word1):
            delete = 1 + self._minDistance(word1, word2, i + 1, j, memo)
            out.append(delete)
        # Replace
        replace = 1 + self._minDistance(word1, word2, i + 1, j + 1, memo)
        out.append(replace)

        memo[(i, j)] = min(out)
        return memo[(i, j)]
