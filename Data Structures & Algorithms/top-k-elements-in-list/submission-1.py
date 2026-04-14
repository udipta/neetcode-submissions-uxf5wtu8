class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = Counter(nums).most_common(k)
        output = [mc[0] for mc in most_common]
        return output