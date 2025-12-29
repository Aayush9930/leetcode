class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        longest = 0
        while r < len(nums):
            while r < len(nums) and nums[r] == 1:
                r += 1
            
            longest = max(longest, (r -l))

            while r < len(nums) and nums[r] != 1:
                r +=1
            l = r
        
        return longest


                