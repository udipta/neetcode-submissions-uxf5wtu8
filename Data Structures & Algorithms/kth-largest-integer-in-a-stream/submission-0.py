import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # in-place transformation into min-heap in linear time
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
