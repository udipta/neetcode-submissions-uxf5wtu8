class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums) # O(n) to build
        longest = 0
        
        for n in nums:
            # Check if 'n' is the start of a sequence
            if (n - 1) not in num_set:
                length = 0
                # Count the streak
                while (n + length) in num_set:
                    length += 1
                
                longest = max(longest, length)
                
        return longest