class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for b in range(len(nums)):
            if target - nums[b] in h:
                return [h[target - nums[b]], b]
            else:
                h[nums[b]] = b
          