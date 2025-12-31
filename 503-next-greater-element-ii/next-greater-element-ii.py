class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []  # monotonic decreasing stack
        out = [-1] * len(nums)
        def helper(nums, stk):
            for i in range(len(nums)):
                if stk:
                    while stk and stk[-1][0] < nums[i]:
                        n, idx = stk.pop()
                        out[idx] = nums[i]
                        
                    stk.append((nums[i], i))
                else:
                    stk.append((nums[i], i))
        
        helper(nums, stk)
        helper(nums, stk)
        return out


