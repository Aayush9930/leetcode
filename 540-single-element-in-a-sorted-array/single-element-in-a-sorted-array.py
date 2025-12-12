class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:       
            mid = (l + r) // 2          

            if (mid == 0 or  nums[mid] != nums[mid - 1]) and (mid ==  len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]

            else:
                left_size = mid - l - 1 if nums[mid] == nums[mid - 1] else mid - l
        
                if left_size % 2 == 0:
                    l = mid + 1 if nums[mid] != nums[mid + 1] else mid + 2

                else:
                        r = mid - 1 if nums[mid] != nums[mid - 1] else mid - 2




