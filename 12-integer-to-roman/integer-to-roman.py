class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],["D", 500],["CM", 900],["M", 1000]]
        res = ""
        symList.reverse()
        i = 0
        while num > 0:
            times = num // symList[i][1]
            res += (symList[i][0] * times)
            num = num % symList[i][1]
            i += 1
        return res