class Solution:
    def equalFrequency(self, word: str) -> bool:
        f = {}
        for c in word:
            f[c] = 1 + f.get(c, 0) 
        print(f)
        for c in word:
            temp = f.copy()
            temp[c] -= 1
            if temp[c] == 0:
                del temp[c]
            print(temp)
            if len(set(temp.values())) == 1:
                return True

        return False