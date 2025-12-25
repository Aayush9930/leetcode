from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)

        for i, v in enumerate(equations):
            x, y = v
            g[x][y] = values[i]
            g[y][x] = 1 / values[i]

        out = []
        for x, y in queries:
            if x not in g or y not in g:
                out.append(-1.0)
                continue
            if x == y:
                out.append(1.0)
                continue

            ans = self.calc(g, x, y, set())
            out.append(ans if ans is not None else -1.0)

        return out

    def calc(self, g, start, end, visited):
        if start == end:
            return 1.0

        visited.add(start)

        for n in g[start]:
            if n not in visited:
                x = self.calc(g, n, end, visited)
                if x is not None:   
                    return g[start][n] * x
        return None
