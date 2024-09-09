class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy
        goal_index = len(nums)-1
        for index in range(len(nums)-1, -1, -1):
            if nums[index]+index >= goal_index:
                goal_index = index
        return goal_index==0

        # top down
        can_reach = [False]*(len(nums))
        can_reach[-1] = True
        for index in range(len(nums)-2, -1, -1):
            for jump_index in range(index+1, min(len(nums), index+nums[index]+1)):
                if can_reach[jump_index]:
                    can_reach[index] = True
                    break
        return can_reach[0]