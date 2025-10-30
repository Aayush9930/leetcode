class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []

        for char in s:
            if len(stk) == 0:
                stk.append(char)

            elif stk[len(stk) -1] != char:
                stk.append(char)

            elif stk[len(stk) - 1] == char:
                stk.pop()

        return "".join(stk)
