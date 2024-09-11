class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach 1: Linear Search
        t: O(n)
        s: O(1)

        Approach 2: Binary Search
        if array was sorted,return the leftmost value - [left]<=[right]
        set mid as min value
        use mid as target and check in left sorted or right sorted portion
        t: O(logn)
        s: O(1)
        """
        left, right = 0, len(nums)-1
        min_num = math.inf
        
        while left<=right:
            mid = left+(right-left)//2
            min_num = min(min_num, nums[mid])

            # right sorted 
            if nums[mid]>nums[right]:
                left = mid+1
            # left sorted
            else:
                right = mid-1
        return min_num
        