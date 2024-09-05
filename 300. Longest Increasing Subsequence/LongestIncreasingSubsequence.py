class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Greedy + Binary Search
        # t: O(nlogn)
        # s: O(n)
        l_sub = []
        for num in nums:
            if not l_sub or l_sub[-1]<num:
                l_sub.append(num)
            else:
                #find the index in l_sub where it should be replaced by num i.e first l_sub[]>=um using binary search
                index = bisect_left(l_sub, num)
                l_sub[index] = num
        return len(l_sub)

        # Bottom Up
        # t: O(n^2)
        # s: O(n)
        cache = [1]*len(nums)
        for start in range(len(nums)-1, -1, -1):
            total = 0
            for end in range(start+1, len(nums), 1):
                if nums[end]>nums[start]:
                    total = max(total, cache[end])
            cache[start] += total
        return max(cache)