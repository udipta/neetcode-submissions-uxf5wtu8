class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        n = len(height)
        
        # O(N) & O(N)
        # prefix_max = [0]*n
        # suffix_max = [0]*n
        # prefix_max[0] = height[0]
        # suffix_max[-1] = height[-1]
        # for i in range(1, n):
        #     prefix_max[i] = max(height[i], prefix_max[i - 1])
        #     suffix_max[n - 1 - i] = max(height[n - 1 - i], suffix_max[n - i])

        # for i in range(n):
        #     total_water += (min(prefix_max[i], suffix_max[i]) - height[i])

        # O(N) & O(1)
        i, j = 0, n - 1
        lmax, rmax = height[i], height[j]
        while i < j:
            if lmax < rmax:
                i += 1
                lmax = max(lmax, height[i])
                total_water += lmax - height[i]
            else:
                j -= 1
                rmax = max(rmax, height[j])
                total_water += rmax - height[j]

        return total_water

        

            
            

