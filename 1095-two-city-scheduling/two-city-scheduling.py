class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return self._twoCitySchedCost(costs, len(costs) // 2, len(costs) // 2, 0, {})

    def _twoCitySchedCost(self, costs, c1, c2, i, memo):
        r = (c1, c2, i)
        if r in memo:
            return memo[r]

        if i == len(costs):
            return 0
        
        out = []

        if c1 > 0:
            x = costs[i][0] + self._twoCitySchedCost(costs, c1 - 1, c2, i + 1, memo)
            out.append(x)
        
        if c2 > 0:
            y = costs[i][1] + self._twoCitySchedCost(costs, c1, c2 - 1, i + 1, memo)
            out.append(y)

        memo[r] =  min(out)
        return memo[r]
        



        
        
