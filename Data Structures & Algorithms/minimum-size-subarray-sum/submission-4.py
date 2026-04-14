class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_window = float('inf')
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_window = min(min_window, right-left+1)
                window_sum -= nums[left]
                left += 1

        if min_window == float('inf'):
            return 0

        return min_window