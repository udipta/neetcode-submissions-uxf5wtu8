class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        result = [1] * n
        for idx in range(n):
            # The mirror index of idx is n - 1 - idx
            mirror_idx = n - 1 - idx
            # 1. Update the current index with the prefix product
            result[idx] *= prefix
            prefix *= nums[idx]

            # 2. Update the mirror index with the suffix product
            result[mirror_idx] *= suffix
            suffix *= nums[mirror_idx]
        return result