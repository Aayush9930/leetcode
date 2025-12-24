class Solution:
    def equalFrequency(self, word: str) -> bool:
        f = {}
        for c in word:
            f[c] = 1 + f.get(c, 0) 

        for c in word:
            f_copy = f.copy()
            f_copy[c] -= 1
            if f_copy[c] == 0:
                del f_copy[c]
            
            if len(set(f_copy.values())) == 1:
                return True
        
        return False 