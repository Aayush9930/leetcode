class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        out = [-1] * len(rains)
        h = {}
        zeroh = []
        for i in range(len(rains)):
            if rains[i] > 0 and rains[i] not in h:
                h[rains[i]] = i
            
            elif rains[i] > 0 and rains[i] in h:    
                idx = h[rains[i]]
                l, r = 0, len(zeroh) - 1
                target = None
                pos = None
                while l <= r:
                    mid = (l + r) // 2
                    if zeroh[mid] > idx:
                        target = zeroh[mid]
                        pos = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                if target == None:
                    return []
                out[target] = rains[i]
                zeroh.pop(pos)
                h[rains[i]] = i

            else:
                zeroh.append(i)
                out[i] = 1
        
        return out