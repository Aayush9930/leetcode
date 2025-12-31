class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []

        for d in num:
            while stk and int(stk[-1]) > int(d) and k > 0:
                stk.pop()
                k -= 1

            stk.append(d)
        
        while k != 0:
            stk.pop()
            k -= 1

        i = 0
        while i < len(stk) and stk[i] == "0":
            i += 1
        
        stk = stk[i:]

        print(stk)

        if not stk:
            return "0"
        
        return "".join(stk)
