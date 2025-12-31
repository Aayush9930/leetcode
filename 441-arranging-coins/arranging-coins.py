class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        last_valid = None
        while l <= r:
            mid = (l + r) // 2 
            size = int((mid * (mid + 1)) / 2)

            if n > size:
                last_valid = mid
                l = mid + 1
            
            elif n < size:
                r = mid - 1
                
            else:
                return mid
        
        return last_valid
        
        
        # count_row = 0
        # row_size = 1

        # while n >= row_size:
        #     n = n - row_size
        #     count_row += 1
        #     row_size += 1
        
        # return count_row
