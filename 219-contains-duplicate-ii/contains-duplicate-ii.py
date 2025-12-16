class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for i in range(len(nums)):
            if nums[i] in h and abs(h[nums[i]] - i) <= k:
                return True
            else:
                h[nums[i]] = i

        return False              