class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if k == 1:
            return ''

        stk = []

        for c in s:
            if not stk:
                stk.append((c, 1))
            else:
                if stk[-1][0] == c:
                    if stk[-1][1] == k - 1:
                        for _ in range(k - 1):
                            stk.pop()
                    else:
                        stk.append((c, stk[-1][1] + 1))
                else:
                    stk.append((c, 1))
        
        res = [ c for c, f in stk ]
        return "".join(res)

