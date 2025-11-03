class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generateParenthesis_helper(n, n)

    def generateParenthesis_helper(self, left, right):
        if left == 0 and right == 0:
            return ['']

        out = []

        # choosing left
        if left > 0:
            rest = self.generateParenthesis_helper(left - 1, right)

            for s in rest:
                out.append('(' + s)
 
        # choosing right iff left < right

        if left < right:
            rest2 = self.generateParenthesis_helper(left, right - 1)

            for s2 in rest2:
                out.append(')' + s2)

        return out
