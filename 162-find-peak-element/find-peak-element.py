class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                l = mid + 1
            
            elif mid == len(nums) - 1:
                if nums[mid - 1] < nums[mid]:
                    return mid
                r = mid - 1

            elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            
            elif nums[mid - 1] > nums[mid]:
                r = mid - 1

            elif  nums[mid] < nums[mid + 1]:
                l = mid + 1

        return l
        
