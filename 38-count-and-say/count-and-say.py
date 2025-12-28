class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        x = self.countAndSay(n - 1)
    
        l, r = 0, 0
        res = ""
        while r < len(x):
            if x[r] == x[l]:
                r += 1
            else:
                res += (str(r - l) + x[l])
                l = r

        res += (str(r - l) + x[l])
        
        return res