class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        for i in range(len(heights)):
            if stk:
                if stk[-1][1] > heights[i]:
                    index = None
                    while stk and stk[-1][1] > heights[i]:
                        idx, h = stk.pop()
                        area = h * (i - idx)
                        max_area = max(max_area, area)
                        index = idx
                    stk.append((index, heights[i]))
                else:
                    stk.append((i, heights[i]))
            else:
                stk.append((i, heights[i]))

        for i, h in stk:
            area = h * (len(heights) - i)
            max_area = max(max_area, area)

        return max_area 