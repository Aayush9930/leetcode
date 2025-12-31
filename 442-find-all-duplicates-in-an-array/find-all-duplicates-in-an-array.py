class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1 # index where i am gonna mark 
            if nums[idx] < 0:
                res.append(abs(nums[i]))
            else: 
                nums[idx] = -nums[idx] # mark negative


        return res
        
        

        
        
        
        
        # f = {}

        # for x in nums:
        #     f[x] = 1 + f.get(x, 0)
        
        # out = []
        # for val in f:
        #     if f[val] == 2:
        #         out.append(val)
            
        # return out