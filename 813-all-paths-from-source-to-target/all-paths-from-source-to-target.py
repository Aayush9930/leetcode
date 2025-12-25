class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self._allPathsSourceTarget(graph, 0, len(graph) - 1, {})

    def _allPathsSourceTarget(self, g, src, dst, memo):
        if src in memo:
            return memo[src]
            
        if src == dst:
            return [[ src ]]
        if g[src] == []:
            return None
        out = []
        for n in g[src]:
            x = self._allPathsSourceTarget(g, n, dst, memo)
            if x != None:
                for p in x:
                    out.append([src, *p])
        memo[src] = out
        return memo[src]