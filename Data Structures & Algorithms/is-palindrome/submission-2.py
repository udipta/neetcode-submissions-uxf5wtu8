class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                ss += ch.lower() 
        
        l = 0
        r = len(ss) - 1
        while l < r and ss[l] == ss[r]:
            l += 1
            r -= 1
        return l >= r