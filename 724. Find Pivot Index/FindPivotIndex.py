class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # t: O(n+n)
        # s: O(1)
        rightsum, leftsum = sum(nums), 0

        for index in range(len(nums)):
            if leftsum==(rightsum-leftsum-nums[index]):
                return index
            leftsum+=nums[index]
        return -1