class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)

        l, r = 1, max_speed
        opt = float('inf')
        while l <= r:
            mid_speed = (l + r) // 2 

            time = 0
            for pile in piles:
                time += math.ceil(pile / mid_speed)
             
            if time > h:
                l = mid_speed + 1
            else:
                opt = min(opt, mid_speed)
                r = mid_speed - 1
        
        return opt