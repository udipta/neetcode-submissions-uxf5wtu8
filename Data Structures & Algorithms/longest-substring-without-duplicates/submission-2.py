class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        max_len = 0
        l = 0
        for r in range(len(s)):
            while s[r] in visited:
                 visited.discard(s[l])
                 l += 1
            visited.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len