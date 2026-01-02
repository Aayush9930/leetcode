class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5, math.ceil(n / 2), (10**9 + 7)) * pow(4, n // 2, (10**9 + 7))) % (10**9 + 7)
    

    def pow(self, x, n):
        if n == 0:
            return 1
        
        res = self.pow(x, n // 2)

        if n % 2 == 0:
            return res * res
        
        else:
            return res * res * x