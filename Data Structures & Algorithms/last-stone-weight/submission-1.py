class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [n*(-1) for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            w = x - y
            if w != 0:
                heapq.heappush(stones, w)
        
        return heapq.heappop(stones) * (-1) if len(stones) == 1 else 0
                