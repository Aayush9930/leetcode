class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        l, m = 0, 0 
        odd = 0

        for r in range(len(nums)):
            # increase the window
            if nums[r] % 2 == 1:
                odd += 1
            
            # decrease my window if the window is invalid
            if odd > k:
                while odd > k:
                    if nums[l] % 2 == 1:
                        odd -= 1
                    l += 1
                    m = l
                
            if odd == k:
                while nums[m] % 2 == 0:
                    m += 1
                res += (m - l + 1)
            
        return res
