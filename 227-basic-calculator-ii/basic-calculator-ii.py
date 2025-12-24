class Solution:
    def calculate(self, s: str) -> int:
        prev_num = 0
        curr_num = 0
        res = 0
        curr_operation = "+"
        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = ""
                while i < len(s) and s[i].isdigit():
                    num = num + s[i]
                    i += 1 
                curr_num = int(num)
                i -= 1

                if curr_operation == "+":
                    res = res + curr_num
                    prev_num = curr_num

                elif curr_operation == "-":
                    res = res - curr_num
                    prev_num = -curr_num
                
                elif curr_operation == "*":
                    res = res - prev_num
                    res += (prev_num * curr_num)
                    prev_num = (prev_num * curr_num)
                
                elif curr_operation == "/":
                    res = res - prev_num
                    res += int(prev_num / curr_num)
                    prev_num = int(prev_num / curr_num)
                
            elif s[i] in "+-*/":
                curr_operation = s[i]
            
            i += 1
        
        return res

