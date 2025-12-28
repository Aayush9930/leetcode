class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        left = 1 
        for right in range(1, len(nums)):
            if nums[right] == nums[right - 1]:
                continue
            else:
                nums[left] = nums[right]
                left += 1
                k += 1
        return k  