class Solution:
    def twoSum(self, nums, target):
        # hashPrev = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in hashPrev:
        #         return [hashPrev[diff], i]
        #     hashPrev[nums[i]] = i
        setNums = {}

        for i in range(len(nums)):
            if (target - nums[i]) in setNums:
                return [i , setNums[target-nums[i]]]
            else:
                setNums[nums[i]] = i