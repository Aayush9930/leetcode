class Solution:
    def decodeString(self, s: str) -> str:
        stk = []

        for c in s:
            if c == "]":
                string = ''
                while stk[-1] != '[':
                    string = stk.pop() + string
                stk.pop()
                number = ''
                while stk and stk[-1].isdigit():
                    number = stk.pop() + number
                
                string = string * int(number)
                stk.append(string)

            else:
                stk.append(c)

        return ("").join(stk)