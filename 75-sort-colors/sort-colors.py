class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        i = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[i] = color
                i += 1
