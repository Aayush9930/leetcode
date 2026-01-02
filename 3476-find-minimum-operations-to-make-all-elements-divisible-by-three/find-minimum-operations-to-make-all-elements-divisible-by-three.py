class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0 
        
        for num in nums:
            divides = num // 3
            low_target = divides * 3
            high_target = divides * 3 + 3
            res += min(num - low_target, high_target - num) 

        return res
