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
        
        print(stk)

        
        while stk and stk[0] == "0":
            stk.pop(0)

        if not stk:
            return "0"
        
        return "".join(stk)
    