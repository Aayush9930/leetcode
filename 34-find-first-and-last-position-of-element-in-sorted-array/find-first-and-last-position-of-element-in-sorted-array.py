class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bound_calc(leftBias):
            l, r  = 0, len(nums) - 1 
            bound = -1
            while l <= r:
                mid = (l + r) // 2

                if target > nums[mid]:
                    l = mid + 1

                elif target < nums[mid]:
                    r = mid - 1
                
                else:
                    bound = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return bound
            
        left_bound = bound_calc(True)
        right_bound =  bound_calc(False)

        return [ left_bound, right_bound ]

