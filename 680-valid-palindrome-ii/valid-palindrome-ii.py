class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        buffer = 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -=1

            else:
                if buffer == 1:
                    # if s[l+1] == s[r]:
                    #     l += 1
                    # elif s[l] == s[r-1]:
                    #     r -= 1
                    # buffer = 0
                    if isPalindrome(s[l:r]) == True:
                        r -= 1
                    elif isPalindrome(s[l+1: r +1]):
                        l += 1 
                    buffer = 0
                else:
                    return False

        return True

def isPalindrome(s):
    l , r = 0, len(s) - 1 

    while l <= r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1

    return True
