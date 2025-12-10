class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        total = 0
        for num in nums:
            total += num
            prefix_sum.append(total)

        seen = {}
        res = 0
        for b in range(len(prefix_sum)):
            if (prefix_sum[b] - k) in seen:
                res += seen[prefix_sum[b] - k]
                seen[prefix_sum[b]] = 1 + seen.get(prefix_sum[b], 0)
            else:
                seen[prefix_sum[b]] = 1 + seen.get(prefix_sum[b], 0)
            
        return res
            