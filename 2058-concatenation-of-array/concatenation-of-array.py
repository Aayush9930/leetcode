class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
        
        # ans = []
        # r = 0
        # for i in range(0,2*len(nums)):
        #     if i < len(nums):
        #         r = i
        #         ans.append(nums[r])
        #     else:
        #         r = i - len(nums)
        #         ans.append(nums[r])
        # return ans