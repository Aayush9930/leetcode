class Solution:
    def convert(self, s: str, numRows: int) -> str:
        out = [ [] for _ in range(numRows) ]

        i = 0
        while i < len(s):
            for j in range(numRows): # 0, 1, 2
                if i >= len(s):
                    break
                out[j].append(s[i])
                i += 1
            
            for j in range(numRows - 2, 0, -1):
                if i >= len(s):
                    break
                out[j].append(s[i])
                i += 1
            
        for i in range(len(out)):
            out[i] = "".join(out[i])

        return "".join(out)


    