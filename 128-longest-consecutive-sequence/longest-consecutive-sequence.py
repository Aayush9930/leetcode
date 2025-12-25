class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        visited = set()
        for num in nums:
            if num - 1 not in s and num not in visited:
                visited.add(num)
                count = 1
                while num + 1 in s:
                    num = num + 1
                    count += 1
                longest = max(count, longest)
        return longest