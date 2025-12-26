class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        first = nums[0]
        rest =  self.permuteUnique(nums[1:])
        out = []
        seen = set()
        for p in rest:
            for i in range(len(p) + 1):
                x = p[:i] + [first] + p[i:]
                temp = tuple(x)
                if temp not in seen:
                    seen.add(temp)
                    out.append(x)
        return out
                

