class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Partition Sort -> 2 pass
        l = 0 
        
        for r in range(len(nums)):   # [0, 0, .....]
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        for r in range(l, len(nums)):
            if nums[r] == 1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            
        
        
        
        # Count Sort / Bucket Sort
        # count = [ 0, 0, 0 ]
        # for num in nums:
        #     count[num] += 1

        # i = 0
        # for j in range(3):
        #     while count[j] != 0:
        #         nums[i] = j
        #         i += 1
        #         count[j] -= 1
        



        