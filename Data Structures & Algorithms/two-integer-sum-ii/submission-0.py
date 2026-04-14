class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < len(numbers) and j >= 0 and j > i:
            if numbers[i] + numbers[j] == target:
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i+1, j+1]