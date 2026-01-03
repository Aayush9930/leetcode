class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[ s[0] ]]
        
        first = s[0]
        rest = self.partition(s[1:])

        out = []
        seen = set()
        for p in rest:
            if tuple([first, *p]) not in seen:
                seen.add(tuple([first, *p]))
                out.append([first, *p])
            string = first
            for i in range(len(p)):
                string = string + p[i]
                if self.isPalindrome(string):
                    incoming = [string] + p[i + 1:]
                    if tuple(incoming) not in seen:
                        seen.add(tuple(incoming))
                        out.append([string] + p[i + 1:])
        return out 

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True


