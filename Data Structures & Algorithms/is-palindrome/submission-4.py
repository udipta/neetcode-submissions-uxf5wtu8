class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                ss += ch.lower() 
        
        l = 0
        n = len(ss)
        mid = n // 2
        while l < mid and ss[l] == ss[n - l - 1]:
            l += 1
        return l >= mid  # True if palindrome else False