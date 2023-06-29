class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        sum, prefixsum = -math.inf, 0
        for n in nums:
            prefixsum += n
            sum = max(prefixsum, sum)
            prefixsum = 0 if prefixsum<0 else prefixsum
        return sum