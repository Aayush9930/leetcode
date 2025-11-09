class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self._minDistance(word1, word2, {})

    
    
    def _minDistance(self, word1: str, word2: str, memo) -> int:
        if (word1, word2) in memo:
            return memo[(word1, word2)]

        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        if word1[0] == word2[0]:
            memo[(word1, word2)] =  self._minDistance(word1[1:], word2[1:], memo)
            return memo[(word1, word2)]
        
        elif word1[0] != word2[0]:
            options = []

            # insert
            insert = 1 + self._minDistance(word1, word2[1:], memo)
            options.append(insert)
            # delete
            delete = 1 + self._minDistance(word1[1:], word2, memo)
            options.append(delete)

            # replace
            replace = 1 + self._minDistance(word1[1:], word2[1:], memo)
            options.append(replace)

            memo[(word1, word2)] = min(options)
            return memo[(word1, word2)]
