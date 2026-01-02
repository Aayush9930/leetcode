class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_odd = 0 
        l = 0
        m = 0
        res = 0

        for r in range(len(nums)):
            # increase my window till valid
            if nums[r] % 2 == 1:
                    count_odd += 1

            while count_odd > k:
                if nums[l] % 2 == 1:
                    count_odd -= 1
                l += 1
                m = l

            if count_odd == k:
                while nums[m] % 2 == 0:
                    m += 1
                res += (m - l + 1)

        return res
                
