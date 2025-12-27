class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        remove_i = []
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                if stk:
                    stk.pop()
                else:
                    remove_i.append(i)
        remove_i = remove_i + stk
        s = list(s)
        for i in remove_i:
            s[i] = ""
        return "".join(s)
        

        
