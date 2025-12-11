class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = {}
        for i in range(len(graph)):
            g[i] = graph[i]

        return self._allPathsSourceTarget(g, 0, len(graph) - 1, {})

    def _allPathsSourceTarget(self, graph, start, dst, memo):
        if start in memo:
            return memo[start]

        if start == dst:
            return [[ dst ]]

        if graph[start] == []:
            return []
        
        out = []
        for n in graph[start]:
            x  = self._allPathsSourceTarget(graph, n, dst, memo)
            for p in x:
                out.append([start, *p])
        
        memo[start] = out
        return memo[start]