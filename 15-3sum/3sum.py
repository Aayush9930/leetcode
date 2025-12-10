class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                continue

            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                total = nums[l] + nums[r]

                if target > total:
                    l += 1
                
                elif target < total:
                    r -= 1
    
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    
        return out
                


