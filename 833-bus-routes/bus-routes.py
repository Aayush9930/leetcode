from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stopToLine = {}

        for line in range(len(routes)):
            for stop in routes[line]:
                if stop in stopToLine:
                    stopToLine[stop].append(line)
                else:
                    stopToLine[stop] = [line]
        
        q = deque([(source, 0)])
        visitedStops = set()
        visitedLines = set()

        if source not in stopToLine or target not in stopToLine:
            return -1

        while q:
            s, l = q.popleft()

            if s == target:
                return l

            for line in stopToLine[s]:
                if line not in visitedLines:
                    visitedLines.add(line)
                    for stop in routes[line]:
                        if stop not in visitedStops:
                            visitedStops.add(stop)
                            q.append((stop, l + 1))
        
        return -1
        