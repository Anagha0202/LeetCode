class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        minops = 0

        for val in counts.values():
            # if val is 1, directly return -1
            if val==1:
                return -1
            # if val is anything else, first remove all the triplets possible
            minops += val//3
            # for eg: if val = 7 and minops = 2
            # 2,2,2 | 2,2,2 | 2
            # Only 1 remains after splitting into triplets which cannot be formed into a pair.
            # So when we have a remainder after splitting into 3's, we are essentially breaking one triplet (minops = 1) and then pairing them (minops = 1+1 -> 1 triplet and 1 pair) and then pairing the remaining number with the one broken from the triplet.
            # Hence 1 pair has to be added when there is a remainder (remainder can be 1 or 2)
             
            if val%3:
                minops += 1
        
        return minops