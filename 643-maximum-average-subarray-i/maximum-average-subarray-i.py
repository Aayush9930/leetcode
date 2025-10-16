class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0

        #initialize the window

        for i in range(k):
            cur_sum += nums[i]

        max_avg = cur_sum / k

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            max_avg = max(max_avg, cur_sum/k) 

        return max_avg


