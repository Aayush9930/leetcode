class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f = {}

        for x in nums:
            f[x] = 1 + f.get(x, 0)
        
        out = []
        for x in f:
            if f[x] > len(nums) // 3:
                out.append(x)
        
        return out
         