class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l , r = 0, 1
        if len(nums)<=1:
            return l+1
        while r<len(nums) and l<=r:
            if nums[l]!=nums[r]:
                l+=1
                nums[l], nums[r] = nums[r], nums[l]
            r+=1
        return l+1