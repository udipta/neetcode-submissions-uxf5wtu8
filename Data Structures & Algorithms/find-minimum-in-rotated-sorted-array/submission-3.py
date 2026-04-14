class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m   # Rotation Detected. check on the 1st half of the list
            else:
                l = m + 1
        return nums[l]