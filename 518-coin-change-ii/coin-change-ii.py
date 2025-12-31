class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self._change(amount, coins, 0, {})

    def _change(self, amount, coins, i, memo):
        if amount == 0:
            return 1
        if amount < 0 or i == len(coins):
            return 0

        key = (i, amount)
        if key in memo:
            return memo[key]

        # option 1: don't use coins[i]
        not_take = self._change(amount, coins, i + 1, memo)
        # option 2: use coins[i] (can reuse it, so i stays same)
        take = self._change(amount - coins[i], coins, i, memo)

        memo[key] = take + not_take
        return memo[key]
        
        
        
        
        
        # if (i, amount) in memo:
        #     return memo[(i, amount)]

        # if amount == 0:
        #     return 1

        # if i == len(coins):
        #     return 0
        
        # total = 0
        # for j in range(0, (amount // coins[i]) + 1):
        #     total += self._change(amount - (coins[i] * j), coins, i + 1, memo)

        # memo[(i, amount)] =  total
        # return memo[(i, amount)]
