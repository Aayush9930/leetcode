class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        possible_i = None
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                possible_i = mid
                l = mid + 1
            
            else:
                r = mid - 1

        if possible_i == None:
            return 0
        return possible_i + 1