class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            max_area = max(max_area, area)
            if heights[i] > heights[j]: j -= 1
            else: i += 1
        return max_area
