class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = [] # [val, min_left]
        curr_min = nums[0]

        for num in nums[1:]:
            while stk and num >= stk[-1][0]:
                stk.pop()
            
            if stk and num > stk[-1][1]:
                return True

            stk.append([num, curr_min])
            curr_min = min(curr_min, num)
        
        return False

