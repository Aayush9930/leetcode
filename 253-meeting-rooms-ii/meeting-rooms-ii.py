class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([ s for s, e in intervals ])
        ends = sorted([ e for s, e in intervals ])
        s, e = 0, 0
        max_meeting = 0
        meeting = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                meeting += 1
                max_meeting = max(max_meeting, meeting)
                s += 1
            elif starts[s] >= ends[e]:
                meeting -= 1
                max_meeting = max(max_meeting, meeting)
                e += 1

        return max_meeting