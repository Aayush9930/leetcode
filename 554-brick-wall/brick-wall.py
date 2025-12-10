class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        h = {}

        for row in wall:
            total = 0
            for num in row[:-1]:
                total += num
                h[total] = 1 + h.get(total, 0)

        gaps = max(h.values()) if h else 0
        
        return len(wall) - gaps