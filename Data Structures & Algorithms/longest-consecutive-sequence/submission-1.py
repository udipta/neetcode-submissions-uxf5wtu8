class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_size = 1
        for num in nums:
            size = 1
            head = num - 1
            while head in nums:
                size += 1
                head -= 1
            max_size = max(max_size, size)
        return max_size
