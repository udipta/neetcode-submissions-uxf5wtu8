class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Try skipping left or right character
                skip_left = s[l + 1:r + 1]
                skip_right = s[l:r]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            l += 1
            r -= 1
        return True