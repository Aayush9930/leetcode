class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return (num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336)
        
        # res = []
        # for i in range(1, num):
        #     if num % i == 0:
        #         res.append(i)

        # return sum(res) == num