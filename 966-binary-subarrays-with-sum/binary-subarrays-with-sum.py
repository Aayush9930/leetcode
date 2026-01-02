class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal == 0:
            l = 0
            res = 0

            for r in range(len(nums)):
                if nums[r] == 0:
                    res += (r - l + 1)
                elif nums[r] == 1:
                    l = r + 1
            return res

        total = 0
        l = 0
        m = 0 
        res = 0

        for r in range(len(nums)):
            # expand the window
            total += nums[r]

            # shrink
            while total > goal:
                total -= nums[l]
                l += 1
                m = l

            # do result counting while equal
            if total == goal:
                while nums[m] != 1:
                    m += 1
                res += m - l + 1
        return res
        
        
        # # normal wrong approach
        # total = 0
        # l = 0 
        # res = 0

        # for r in range(len(nums)):
        #     # increse
        #     total += nums[r]

        #     # count while shrinking
        #     while l < len(nums) and total == goal:
        #         res += 1
        #         total -= nums[l]
        #         l += 1
        # return res

            

    