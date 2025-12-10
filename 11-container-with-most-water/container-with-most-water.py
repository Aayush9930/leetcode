class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0   
        r = len(height) - 1
        max_area = 0
        while l <= r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)

            if height[l] > height[r]:
                r -= 1
            
            elif height[l] < height[r]:
                l += 1
            
            else:
                l += 1
        














        # l = 0
        # r = len(height) - 1
        # max_area = 0
        # while r>l:
        #     if len(height) == 2:
        #         max_area = 1* min(height[l], height[r])
        #     if height[r] > height[l]:
        #         max_area = max(max_area, (r-l)* min(height[l], height[r]))
        #         l += 1
        #     elif height[r] == height[l]:
        #         max_area = max(max_area, (r-l)* min(height[l], height[r]))
        #         l+= 1
        #         r-=1
        #     else:
        #         max_area = max(max_area, ((r-l)* min(height[l], height[r])))
        #         r -= 1
            
        # return max_area















        l = 0
        r = len(height) - 1
        max_area = 0
        while r > l:
            if height[r]> height[l]:
                max_area = max(max_area, min(height[r], height[l]) * (r-l))
                l+=1
            elif  height[r] < height[l]:
                max_area = max(max_area, min(height[r], height[l]) * (r-l))
                r -=1
            else:
                max_area = max(max_area, min(height[r], height[l]) * (r-l))
                r-=1
                l+=1
        return max_area













            



