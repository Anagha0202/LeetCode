class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (len(nums)<1) or (len(nums)==1 and nums[0]==val):
            return 0 
        l, r = 0, 0
        while r<len(nums) and l<=r:
            if nums[r] == val:
                r+=1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r+=1
        return l