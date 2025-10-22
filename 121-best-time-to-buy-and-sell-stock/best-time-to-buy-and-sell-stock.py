class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_p = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                max_p = max(max_p, prices[r] - prices[l])

            elif prices[r] <= prices[l]:
                l = r

        return max_p
        
        
        
        
        
        
        
        # l = 0
        # max_profit = 0
        # for r in range(1, len(prices)):
        #     if prices[r] - prices[l] < 0:
        #         l=r
        #     else:
        #         if max_profit < prices[r] - prices[l]:
        #             max_profit = prices[r] - prices[l]
        # return max_profit
















        l = 0 
        max_profit = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                # max_profit = max(max_profit, )
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                
        return max_profit