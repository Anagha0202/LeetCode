class Solution:
    def rob(self, nums: List[int]) -> int:
        # houses 0 and n-1 are adjacent to each other which means, if we rob house 0, then we cannot rob house n-1 and vice versa. 
        # we split the input into 2 houses lists, one having house 0 and one having house n-1
        # t: O(n)
        # s: O(n)
        def bottom_up(start_idx, end_idx, nums):
            robbed = [0]*(len(nums)+2)
            for house in range(end_idx, start_idx-1, -1):
                robbed[house] = max(nums[house]+robbed[house+2], robbed[house+1])
            return robbed[start_idx]
        
        if len(nums)<=2:
            return max(nums)
        return max(bottom_up(0,len(nums)-2, nums), bottom_up(1, len(nums)-1, nums))