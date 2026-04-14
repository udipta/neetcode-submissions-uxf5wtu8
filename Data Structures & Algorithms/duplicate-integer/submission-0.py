class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return bool(len(set(nums)) != len(nums))