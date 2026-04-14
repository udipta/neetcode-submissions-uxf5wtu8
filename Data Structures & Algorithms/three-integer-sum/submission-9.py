class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1
            target = -nums[k]
            # Two Sum
            while i < j:
                if nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
        return res