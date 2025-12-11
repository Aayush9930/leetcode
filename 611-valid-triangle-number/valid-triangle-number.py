class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for k in range(2, len(nums)):
            i, j = 0, k - 1

            while i < j:
                total = nums[i] + nums[j]

                if total > nums[k]:  # valid triangle
                    count += (j - i)
                    j -= 1
                
                elif total <= nums[k]:
                    i += 1
        
        return count
                
