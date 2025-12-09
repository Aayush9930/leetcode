class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= out[-1][1]:
                x = [out[-1][0], max(out[-1][1], intervals[i][1])]
                out.pop()
                out.append(x)
            else:
                out.append(intervals[i])

        return out

