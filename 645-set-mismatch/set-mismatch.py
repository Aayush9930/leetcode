class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        out = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                out.append(abs(x))
            else:
                nums[abs(x) - 1] = -nums[abs(x) - 1]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                out.append(i + 1)
        
        return out
