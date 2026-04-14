class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of elements
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num
            # print(complement)

            # Check if the complement exists in the dictionary
            if complement in num_indices:
                return [num_indices[complement], i]

            # Store the index of the current element in the dictionary
            num_indices[num] = i

