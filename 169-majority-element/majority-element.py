class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Apprach 1 to achieve O(1) space
        # nums.sort()
        # return nums[len(nums) // 2]

        count = 0
        candidate = None

        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            
            elif x == candidate:
                count += 1
            
            elif x != candidate:
                count -= 1
        return candidate


