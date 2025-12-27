class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        for c in s:
            freq_s[c] += 1
        for c in t:
            freq_t[c] += 1
        res = 0
        for c in freq_s:
            if freq_s[c] > freq_t[c]:
                res += freq_s[c] - freq_t[c]
        return res
