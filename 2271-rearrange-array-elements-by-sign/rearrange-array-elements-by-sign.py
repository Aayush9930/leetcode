class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        x, y = 0, 0
        out = []
        while x < len(pos) and y < len(neg):
            out.append(pos[x])
            x += 1
            out.append(neg[y])
            y += 1


        return out