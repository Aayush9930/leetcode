class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        out = []

        for a in range(len(nums)):
            if a > 0 and nums[a - 1] == nums[a]:
                continue
            
            for b in range(a + 1, len(nums)):
                if b > a + 1 and nums[b - 1] == nums[b]:
                    continue

                c, d = b + 1, len(nums) - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    if total > target:
                        d -= 1
                    elif total < target:
                        c += 1
                    else:
                        out.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < len(nums) and nums[c - 1] == nums[c]:
                            c += 1
        return out 