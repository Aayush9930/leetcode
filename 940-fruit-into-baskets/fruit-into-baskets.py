class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maximum = 0
        h = {}

        l = 0 

        for r in range(len(fruits)):
            h[fruits[r]] = 1 + h.get(fruits[r], 0)

            if len(h) <= 2:
                maximum = max(maximum, r - l + 1)

            elif len(h) > 2:
                    while len(h) > 2:
                        h[fruits[l]] = h.get(fruits[l], 0) - 1
                        if h[fruits[l]] == 0:
                            del h[fruits[l]]
                        l += 1
        return maximum
