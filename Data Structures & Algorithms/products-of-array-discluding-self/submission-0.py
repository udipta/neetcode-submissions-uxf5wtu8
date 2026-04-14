class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        result = [1] * n
        # 1. Update the current index with the prefix product
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]


        # 2. Update the mirror index with the suffix product
        for i in range(n):
            # The mirror index of i is n - 1 - i
            result[n - 1 - i] *= suffix
            suffix *= nums[n - 1 - i]
        return result