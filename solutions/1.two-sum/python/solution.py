class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The difference between the current number and the target
        # is saved for every index.
        # If the current number is a stored difference,
        # then the pair adds to the target.

        # Map difference to index
        difference_index = {}

        for i, num in enumerate(nums):
            if num in difference_index:
                # Found
                return [difference_index[num], i]

            difference = target - num
            difference_index[difference] = i

        