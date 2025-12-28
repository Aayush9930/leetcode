class Solution:
    def climbStairs(self, n: int) -> int:
        return self._climbStairs(n, {})

    def _climbStairs(self, n, memo) -> int:
        if n in memo:
            return memo[n]

        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        memo[n] =  self._climbStairs(n - 1, memo) + self._climbStairs(n - 2, memo)
        return memo[n]
