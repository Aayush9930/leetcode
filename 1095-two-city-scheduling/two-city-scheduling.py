class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = int(len(costs) / 2)
        return self._twoCitySchedCost(costs, n, n, 0, {})
    
    def _twoCitySchedCost(self, cost, na, nb, i, memo):
        m = (na, nb, i)
        if m in memo:
            return memo[m]

        if na == 0 and nb == 0:
            return 0
        
        first = cost[i]
        out = []
        if na > 0:
            x = first[0] + self._twoCitySchedCost(cost, na -1, nb, i + 1, memo)
            out.append(x)
        
        if nb > 0:
            y = first[1] + self._twoCitySchedCost(cost, na, nb - 1, i + 1, memo)
            out.append(y)
        
        memo[m] =  min(out)
        return memo[m]


