class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        if len(pattern) != len(s):
            return False

        wordToChar = {}
        charToWord = {}

        for c, w in zip(pattern, s):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        
        return True

        