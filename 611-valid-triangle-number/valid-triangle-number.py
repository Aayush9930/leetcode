class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()

        res = 0
        for k in range(2, len(nums)):
            i, j = 0, k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                
                elif nums[i] + nums[j] <= nums[k]:
                    i += 1
        return res