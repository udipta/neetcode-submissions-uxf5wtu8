from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

        # 1. DEFINE STATE
        q = deque()
        left = 0
        result = []
        
        for right in range(len(nums)):
            # 2. EXPAND: Add the new element to the state
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # 3. SHRINK: While the window is "Bad" (Invalid)
            while right - left + 1 > k:
                if q[0] == left:
                    q.popleft()
                left += 1

            # 4. UPDATE RESULT: The window is now "Good". Record the metric.
            if (right - left + 1) == k:
                result.append(nums[q[0]])
        return result





