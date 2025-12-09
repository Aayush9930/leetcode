class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []

        for c in s:
            if stk:
                if stk[-1][0] == c:
                    new = stk[-1][1] + 1
                    stk.append((c, new))

                    if new == k:
                        for _ in range(k):
                            stk.pop()
                else:
                    stk.append((c, 1))
            else:
                stk.append((c, 1))
        print(stk)
        out = []
        for c, l in stk:
            out.append(c)

        return ''.join(out)
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stk = []
        # seen = 0
        # for c in s:
        #     if stk:
        #         if stk[-1] != c:
        #             seen = 0
        #             stk.append(c)
        #             seen += 1
        #         else:
        #             stk.append(c)
        #             seen += 1

        #             if seen == k:
        #                 for _ in range(k):
        #                     stk.pop()
        #                 seen = 0
        #     else:
        #         stk.append(c)
        #         seen += 1
        # x = "".join(stk)
        # if x == s:
        #     return s

        # return self.removeDuplicates(x, k)