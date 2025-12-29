class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        m = float('-inf')
        memo = {}
        for i in range(len(energy)):
            x = self._maximumEnergy(energy, k, i, memo)
            m = max(m, x)
        return m
    
    def _maximumEnergy(self, energy, k, i, memo):
        if i in memo:
            return memo[i]
        
        if i >= len(energy):
            return 0 

        memo[i] = energy[i] + self._maximumEnergy(energy, k, i + k, memo)
        return memo[i]