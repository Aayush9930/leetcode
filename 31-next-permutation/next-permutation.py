class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1st: finding the break point index 
        bp = None
        for i in range(len(nums) - 2, -1, -1):  # O(n)
            if nums[i] < nums[i + 1]:
                bp = i
                break
        
        if bp == None:
            l, r = 0, len(nums) - 1
 
            while l <= r:    #O(n)
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return

        
        # 2nd: from [bp + 1 : ] find the smallest element greater than bp element 
        
        for i in range(len(nums) - 1, bp, -1):  #O(n)
            if nums[bp]  < nums[i]:
                nums[bp], nums[i] = nums[i], nums[bp]
                break
        
        # 3rd: reverse [bp + 1 : ]
        l, r = bp + 1, len(nums) - 1
 
        while l <= r:    #O(n)
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        


     