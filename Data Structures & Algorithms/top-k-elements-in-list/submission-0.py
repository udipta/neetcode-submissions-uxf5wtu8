class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = Counter(nums).most_common()
        output = [most_common[i][0] for i in range(k)]
        return output