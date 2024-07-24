class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach 2:
        return not len(nums) == len(set(nums))

        # Approach 1: 
        counts = {}
        for num in nums:
            if num in counts:
                return True
            counts[num] = 1
        return False