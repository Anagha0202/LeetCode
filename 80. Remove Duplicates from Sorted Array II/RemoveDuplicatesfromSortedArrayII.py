class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r<len(nums):
            count = 1
            # counting duplicates of a number 
            while r+1<len(nums) and nums[r]==nums[r+1]:
                count+=1
                r+=1
            # copying into left either 2 or count times 
            for i in range(min(2, count)):
                nums[l] = nums[r] #as r points to the end of the streak
                l+=1
            # moving r to the beginning of next streak 
            r+=1
        return l