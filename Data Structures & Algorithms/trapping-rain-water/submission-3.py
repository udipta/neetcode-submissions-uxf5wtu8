class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        n = len(height)

        # O(N) & O(1)
        l, r = 0, n - 1
        lmax, rmax = height[l], height[r]
        while l < r:
            if lmax < rmax: # Move Right
                l += 1
                lmax = max(lmax, height[l])
                total_water += lmax - height[l]
            else: # Move Left
                r -= 1
                rmax = max(rmax, height[r])
                total_water += rmax - height[r]

        return total_water

        

            
            

