class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = defaultdict(int)
        m, c = 0, 1
        for i in nums:
            count[i] += 1
            if count[i]==m:
                c+=1
            elif count[i]>m:
                m=count[i]
                c=1
        return m*c