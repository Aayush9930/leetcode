class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []    
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if stk:
                while stk and stk[-1][0] < temperatures[i]:
                    t, idx = stk.pop()
                    res[idx] = i - idx
                stk.append((temperatures[i], i))
            
            else:
                stk.append((temperatures[i], i))
        return res