class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        countDiffInt = {}
        l, m = 0, 0
        res = 0

        for r in range(len(nums)):
            # increase the window
            countDiffInt[nums[r]] = 1 + countDiffInt.get(nums[r], 0)
            
            if len(countDiffInt) > k:
                # decrease the window while invalid
                while len(countDiffInt) > k:
                    countDiffInt[nums[m]] -= 1
                    if countDiffInt[nums[m]] == 0:
                        del countDiffInt[nums[m]]
                    m += 1
                l = m 

            # while valid update the result
            if len(countDiffInt) == k:
                while countDiffInt[nums[m]] > 1:
                    countDiffInt[nums[m]] -= 1
                    m += 1
                res += (m - l + 1)
        return res