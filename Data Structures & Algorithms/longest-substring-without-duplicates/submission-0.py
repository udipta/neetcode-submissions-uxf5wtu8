class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        max_len = 0
        j = 0
        for i in range(len(s)):
            while s[i] in visited:
                 visited.discard(s[j])
                 j += 1
            visited.add(s[i])
            max_len = max(max_len, i - j + 1)
        return max_len