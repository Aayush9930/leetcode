class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        max_prod = nums[0]
        res = nums[0]  
        for i in range(1, len(nums)):
            temp = max_prod * nums[i]
            max_prod = max(max_prod * nums[i], min_prod * nums[i], nums[i])
            min_prod = min(temp, min_prod * nums[i], nums[i])
            res = max(res, max_prod)
        return res

