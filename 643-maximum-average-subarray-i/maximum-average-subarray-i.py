class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for i in range(k):
            total += nums[i]
        
        max_avg = total / k
        
        l = 0
        for r in range(k, len(nums)):
            total += nums[r] 
            total -= nums[l]
            l += 1
            avg = total / k
            max_avg = max(max_avg, avg)
        
        return max_avg