class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kdane's algo
        curr_sum = 0
        m = float('-inf')
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += num
            m = max(m, curr_sum)

        return m


