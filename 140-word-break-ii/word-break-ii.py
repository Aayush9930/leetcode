class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        x = self._wordBreak(s, wordDict, 0, {})
        out = []
        for p in x:
            out.append(" ".join(p))
        return out

    def _wordBreak(self, s, wordDict, i, memo):
        if i in memo:
            return memo[i]

        if i == len(s):
            return [[]]
        out = []
        for word in wordDict:
            if s.startswith(word, i):
                x = self._wordBreak(s, wordDict, i + len(word), memo)
                for p in x:
                    out.append([word, *p])
        memo[i] = out
        return memo[i]