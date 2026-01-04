class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == dividend:
            return 1

        res = 0
        sign = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = True
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            count = 0       # how many times i can subtract the divisor from the dividend
            while dividend > (divisor << count + 1):
                count += 1
            res += (1 << count) 
            dividend = dividend - (divisor << count)
        
        if res == (1 << 31) and sign == False:
            return (1 << 31) - 1
        
        elif res == (1 << 31) and sign == True:
            return -(1 << 31)
        
        return res if sign == False else -res
        

