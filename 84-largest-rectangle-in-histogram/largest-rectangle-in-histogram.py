class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        
        for i in range(len(heights)):
            if stk:
                temp = None
                while stk and stk[-1][1] > heights[i]:
                    area = stk[-1][1] * (i - stk[-1][0])
                    max_area = max(max_area, area)
                    temp = stk.pop()
                
                if temp == None:
                    stk.append((i, heights[i]))
                else:
                    stk.append((temp[0], heights[i]))
            else:
                stk.append((i, heights[i]))
        
        for t in stk:
            area = (len(heights) - t[0]) * t[1]
            max_area = max(max_area, area)

        return max_area

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stk = []
        # max_area = 0 
        # for i, height in enumerate(heights):
        #     if stk:
        #         temp = None
        #         while stk and stk[-1][1] > height:
        #             temp = stk.pop()
        #             max_area = max(max_area, temp[1] * (i - temp[0]))
                
        #         stk.append([temp[0] if temp != None else i, height])
                
        #     else:
        #         stk.append([i, height])

        # if stk:
        #     while stk:
        #         x = stk.pop()
        #         max_area = max(max_area, x[1] * (len(heights) - x[0]))
        
        # return max_area



        # if len(heights) == 1:
        #     return heights[0]
        # if len(heights) == 0:
        #     return 0

        # out = []

        # for i in range(len(heights)):
        #     if i == 0:
        #         r = i + 1
        #         while r < len(heights) and heights[r] >= heights[i]:
        #             r += 1 
        #         out.append(heights[i] * (r - i))
            
        #     elif i == len(heights) - 1:
        #         l = i - 1
        #         while l >= 0 and heights[l] >= heights[i]:
        #             l -= 1
        #         out.append(heights[i] * (i - l))

        #     else:
        #         r, l = i + 1, i - 1
        #         while l >= 0 and heights[l] >= heights[i]:
        #             l -= 1
        #         while r < len(heights) and heights[r] >= heights[i]:
        #             r += 1 
        #         out.append(heights[i] * (r - l - 1))
        # return max(out)