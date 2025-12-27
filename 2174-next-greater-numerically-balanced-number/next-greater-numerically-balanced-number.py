class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 1224445):
            if self.isBalanced(i) == True:
                return i
        
    def isBalanced(self, n):
        f = [0] * 10
        while n > 0:
            f[n % 10] += 1
            n = n // 10
        for i in range(len(f)):
            if f[i] != 0 and f[i] != i:
                return False
        return True