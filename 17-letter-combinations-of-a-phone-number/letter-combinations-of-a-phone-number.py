class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        g = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        return self._letterCombinations(digits, g)

    def _letterCombinations(self, digits, g):
        if digits == '':
            return [""]
        
        first = digits[0]
        rest = self._letterCombinations(digits[1:], g)

        out = []
        for c in g[int(first)]:
            for p in rest:
                out.append(c + p)
        
        return out
