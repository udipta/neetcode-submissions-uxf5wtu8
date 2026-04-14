class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_s = ''
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                valid_s += ch.lower()

        return valid_s == valid_s[::-1]