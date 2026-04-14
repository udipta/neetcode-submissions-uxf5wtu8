class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i+1, min(i+k+1, len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False