class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, min(len(nums), i + k + 1)):
        #         if nums[j] == nums[j]:
        #             return True
        # return False

        # Instead of checking all pairs, 
        # we can store the most recent index of each value in a hash map
        d = dict()
        for i, n in enumerate(nums):
            # distance to its last occurrence is within k
            if n in d and i - d[n] <= k:    # "at most k"
                return True
            d[n] = i    # store the current index
        return False

