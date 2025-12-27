class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        x =  self._coinChange(coins, amount, {})
        if x == float('inf'):
            return -1 
        return x

    def _coinChange(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0 
        
        if amount < 0:
            return float('inf')
        
        minimum = float('inf')
        for coin in coins:
            x = self._coinChange(coins, amount - coin, memo)
            minimum = min(minimum, x)

        memo[amount] =  minimum + 1
        return memo[amount]

#T : O(amount * n)
#S : O(amount)