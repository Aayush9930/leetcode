class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:   
        a = set(aliceSizes)
        opt = (sum(aliceSizes) + sum(bobSizes)) // 2
        bobtotal = sum(bobSizes)
        for s in bobSizes:
            if (opt - (bobtotal - s)) in a:
                return [(opt - (bobtotal - s)), s]
        