class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1

            elif target < nums[mid]:
                r = mid - 1 

            else:
                l, r = mid, mid
                while l >= 0 and nums[l] == nums[mid]:
                    l -= 1
                while r < len(nums) and nums[r] == nums[mid]:
                    r += 1
                
                return [l + 1, r - 1]
            
        return [-1, -1]

                 