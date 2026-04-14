class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for n in nums2:
            tmp = n
            for i in range(m):
                if tmp < nums1[i]:
                    nums1[i],tmp = tmp, nums1[i]
            nums1[m] = tmp
            m += 1
            