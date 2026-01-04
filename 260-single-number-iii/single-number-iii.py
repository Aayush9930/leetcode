class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        out = 0
        for num in nums:
            out = out ^ num
        
        out = (out & (out - 1)) ^ out       # 0010 

        b1 = 0
        b2 = 0

        for num in nums:
            if (out & num) > 0:
                b1 = b1 ^ num
            else:
                b2 = b2 ^ num
        return [b1, b2]