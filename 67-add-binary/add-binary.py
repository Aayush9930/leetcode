class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = len(a) - 1, len(b) - 1
        carry = 0
        out = ""
        while x >= 0 and y >= 0:
            if int(a[x]) + int(b[y]) + carry == 3:
                out = "1" + out
                carry = 1
            elif int(a[x]) + int(b[y]) + carry == 2:
                out = "0" + out
                carry = 1 
            
            elif int(a[x]) + int(b[y]) + carry == 1:
                out = "1" + out
                carry = 0

            elif int(a[x]) + int(b[y]) + carry == 0:
                out = "0" + out
                carry = 0
            
            x -= 1
            y-= 1
        
        if y >= 0:
            while y >= 0:
                if int(b[y]) + carry == 2:
                    out = "0" + out
                    carry = 1
                elif int(b[y]) + carry == 1:
                    out = "1" + out
                    carry = 0
                elif int(b[y]) + carry == 0:
                    out = "0" + out
                    carry = 0
                
                y -= 1
        if x >= 0:
            while x >= 0:
                if int(a[x]) + carry == 2:
                    out = "0" + out
                    carry = 1
                elif int(a[x]) + carry == 1:
                    out = "1" + out
                    carry = 0
                elif int(a[x]) + carry == 0:
                    out = "0" + out
                    carry = 0
                x -= 1

        if carry == 1:
            out = '1' + out

        return out