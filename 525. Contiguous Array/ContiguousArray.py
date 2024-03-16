class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Cannot use count1 and count0 because 
        # Eg. [0,0,0,1,1,0,0] 
        # at index 4, it should find max length of 4 as starting from index 1 to 4 
        # there is equal counts. But count0=3 and count1=2
        # The count of 1's and 0's need to counter each other
        # countMap dict tracks the counts and the indexes at which we calcualted that count
        # countMap = {count:index}
        count = 0
        maxLen = 0
        countMap = {0:-1} # initially count=0 before we start the list, so count is 0 at index -1
        for i in range(len(nums)):
            if nums[i]==0:
                count -= 1
            else: count += 1
            if count in countMap:
                maxLen = max(maxLen, i-countMap[count])
            else:
                countMap[count] = i
        return maxLen