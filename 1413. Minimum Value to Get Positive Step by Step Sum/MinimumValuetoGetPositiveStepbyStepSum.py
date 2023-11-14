class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Using prefix sum
        # find the prefix sum until the end and at each step choose the smallest value as the startValue
        # returning 1 over the startValue will ensure that the sum never goes below 1

        # Time:O(n)
        # Space:O(1)

        startValue = 0
        s = 0

        for n in nums:
            s += n
            startValue = min(startValue, s)
        
        return (1-startValue)
