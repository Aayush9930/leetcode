class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def find_winner(idx, lst, k):
            if len(lst) == 1:
                return lst[0] + 1
            evict_idx = (idx + k - 1) % len(lst)
            lst.pop(evict_idx)
            return find_winner(evict_idx, lst, k)
        
        lst = [ i for i in range(n) ]
        return find_winner(0, lst, k)