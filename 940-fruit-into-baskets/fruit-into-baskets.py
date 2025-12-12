class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h = {}
        l = 0
        res = 0
        for r in range(len(fruits)):
            h[fruits[r]] = 1 + h.get(fruits[r], 0)

            if len(h) > 2:
                while len(h) > 2:
                    h[fruits[l]] -= 1
                    if h[fruits[l]] == 0:
                        del h[fruits[l]]
                    l += 1
            
            res = max(res, r - l + 1)
        
        return res

