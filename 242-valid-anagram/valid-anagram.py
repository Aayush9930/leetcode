class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        for c in s:
            h1[c] = 1 + h1.get(c, 0)
        
        h2 = {}
        for c in t:
            h2[c] = 1 + h2.get(c, 0)
        
        if h1 == h2:
            return True 
        
        return False 