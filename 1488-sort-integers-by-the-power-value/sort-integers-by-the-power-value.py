class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def findPower(n, memo):
            if n in memo:
                return memo[n]

            if n == 1:
                return 0

            if n % 2 == 0:
                memo[n] =  1 + findPower(n / 2, memo)
                return memo[n]
            
            else:
                memo[n] =  1 + findPower(3 * n + 1, memo)
                return memo[n]

        out = []
        for i in range(lo, hi + 1):
            x = findPower(i, memo)
            out.append((x, i))
        
        out.sort()
        
        return out[k - 1][1]
