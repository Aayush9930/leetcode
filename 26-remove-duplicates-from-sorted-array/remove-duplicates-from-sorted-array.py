class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(len(nums)):
            if r > 0 and nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            else:
                continue
        return l