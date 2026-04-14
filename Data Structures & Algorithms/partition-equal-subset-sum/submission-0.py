class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If the total sum is odd, we can't split the array into two equal subsets
        if total_sum % 2 != 0:
            return False

        # The target sum we are trying to find in a subset
        target_sum = total_sum // 2

        # Initialize a DP array to track possible sums
        dp = [False] * (target_sum + 1)
        dp[0] = True  # Base case: A sum of 0 is always possible (with an empty subset)

        # Iterate through each number in the array
        for num in nums:
            # Update the DP array from right to left to avoid using the same number twice
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        # The answer is whether we can get the target_sum
        return dp[target_sum]