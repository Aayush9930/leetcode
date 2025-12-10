class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_sum(n):
            total = 0
            while n != 0:
                x = n % 10
                total += x * x
                n = n // 10 

            return total
        
        num_set = set()

        while True:
            x = calculate_sum(n)
            if x in num_set:
                return False
            num_set.add(x)
            if x == 1:
                return True
            n = x
            
