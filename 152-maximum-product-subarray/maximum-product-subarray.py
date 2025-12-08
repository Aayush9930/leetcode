class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd = 1, 1
        
        res = nums[0]

        for num in nums:
            tmp = maxProd * num
            maxProd = max(maxProd * num, minProd * num, num) # [-1,8]
            minProd = min(tmp, minProd * num, num)
            print(maxProd, minProd)
            res = max(res, maxProd)
        
        return res
        
            