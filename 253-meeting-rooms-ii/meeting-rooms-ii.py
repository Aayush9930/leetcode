class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_mr = 0
        count = 0
        start = sorted([ x for x, y in intervals ])
        ends = sorted([ y for x, y in intervals ])
        s = e = 0

        while s < len(start):
            if start[s] < ends[e]:
                count += 1
                s += 1
            elif start[s] > ends[e]:
                count -= 1
                e += 1
            else:   
                count -= 1
                e += 1

            max_mr = max(max_mr, count)

        return max_mr
