class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]:
                continue
            # 3-Sum
            for k in range(l+1, len(nums)):
                if k > l+1 and nums[k] == nums[k-1]:
                    continue
                # 2-Sum
                i = k + 1
                j = len(nums) - 1
                while i < j:
                    if nums[i] + nums[j] + nums[l] + nums[k] > target:
                        j -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[k] < target:
                        i += 1
                    else:
                        res.append([nums[l], nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
        return res