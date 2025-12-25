class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        x = self._wordBreak(s, wordDict)
        out = []
        for p in x:
            out.append(" ".join(p))
        return out

    def _wordBreak(self, s, wordDict):
        if s == '':
            return [[]]
        out = []
        for word in wordDict:
            if s.startswith(word):
                x = self._wordBreak(s[len(word):], wordDict)
                for p in x:
                    out.append([word, *p])
        return out
