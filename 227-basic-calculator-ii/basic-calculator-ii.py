class Solution:
    def calculate(self, s: str) -> int:
        prev = curr = res = 0
        curr_operation = "+"
        i = 0

        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1

                if curr_operation == "+":
                    res += curr
                    prev = curr
                
                elif curr_operation == "-":
                    res -= curr
                    prev = -curr
                
                elif curr_operation == "*":
                    res -= prev
                    res += curr * prev
                    prev = curr * prev
                
                elif curr_operation == "/":
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)
                
                curr = 0
                i += 1

            elif s[i] != " ":
                curr_operation = s[i]
                i += 1

            else:
                i += 1
        return res 