class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        max_l, max_r = height[l], height[r]
        trap = 0

        while l <= r:
            if max_l >= max_r:
                water = max_r - height[r]
                if water > 0:
                    trap += water
                max_r = max(max_r, height[r])
                r -= 1
                
            elif max_l < max_r:
                water = max_l - height[l]
                if water > 0:
                    trap += water
                max_l = max(max_l, height[l])
                l += 1
        return trap  
        