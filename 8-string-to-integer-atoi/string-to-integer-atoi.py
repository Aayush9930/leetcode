class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        i = 0 
        while i < len(s) and s[i] == " ":
            i += 1
        
        sign = True # true -> +ve 

        if i < len(s) and (s[i] == "+" or s[i] == '-'):
            sign = True if s[i] == '+' else False
            i += 1
        
        while i < len(s) and s[i] == "0":
            i += 1 

        num = 0
        while i < len(s):
            if not s[i].isdigit():
                break
            num = num * 10 + int(s[i])
            i += 1
        
        num = num if sign == True else -num

        if num > (2**31) - 1:
            return (2**31) - 1
        
        if num < -(2**31):
            return -(2**31)

        return num
        