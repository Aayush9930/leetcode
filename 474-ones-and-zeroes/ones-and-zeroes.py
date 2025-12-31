class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self._findMaxForm(strs, m, n, 0, {})


    def _findMaxForm(self, strs, m, n, i, memo):        
        x = (m, n, i)

        if x in memo:
            return memo[x]

        if m == 0 and n == 0:
            return 0
        
        if i == len(strs):
            return 0
        
        f = {}
        for c in strs[i]:
            f[c] = 1 + f.get(c, 0)
        
        out = []
        if (f.get("0", 0) <= m) and ("1" not in f or f["1"] <= n):
            take = 1 + self._findMaxForm(strs, m - f.get("0", 0), n - f.get("1", 0), i + 1, memo)
            out.append(take)

        not_take = self._findMaxForm(strs, m, n, i + 1, memo)
        out.append(not_take)

        memo[x] =  max(out)
        return memo[x]