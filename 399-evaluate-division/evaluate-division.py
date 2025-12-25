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
                out.append(-1)
                continue
            if x == y:
                if x in g:
                    out.append(1)
                    continue
            else:
                x = self.calc(g, x, y, None, set())
                if x:
                    out.append(x)
                else:
                    out.append(-1)
        return out 

    def calc(self, g, start, end, parent, visited):
        if start == end:
            return 1
        
        visited.add(start)
        found = None
        for n in g[start]:
            if n != parent and n not in visited:
                x = self.calc(g, n, end, start, visited)
                if x != None:
                    return g[start][n] * x
        visited.remove(start)
    
            

