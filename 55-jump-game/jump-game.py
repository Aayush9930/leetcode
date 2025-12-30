class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPost = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= goalPost:
                goalPost = i
        
        if goalPost == 0:
            return True
        return False



    # def canJump(self, nums: List[int]) -> bool:
    #     return self._canJump(nums, 0, {})
    
    # def _canJump(self, nums, i, memo):
    #     if i in memo:
    #         return memo[i]

    #     if i >= len(nums) - 1:
    #         return True

    #     for s in range(1, nums[i] + 1):
    #         if  self._canJump(nums, i + s, memo) == True:
    #             memo[i] =  True
    #             return memo[i]

    #     memo[i] =  False
    #     return memo[i]
