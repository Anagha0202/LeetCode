class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Time: O(nlogn)
        # Space: O(n)
        minheap = []
        for i, num in enumerate(nums):
            if num==0:
                heapq.heappush(minheap, (mapping[num], i, num))
                continue
            mapped = 0
            place, n = 1, num
            while n>0:
                d = n%10
                n = n//10
                mapped = mapped + place*mapping[d]
                place = place*10
            heapq.heappush(minheap, (mapped, i, num))
        # print(minheap)
        ans = []
        while minheap:
            ans.append(heapq.heappop(minheap)[2])
        return ans



        minheap = []
        for i, num in enumerate(nums):
            mapped = ""
            for n in str(num):
                mapped += str(mapping[int(n)])
            heapq.heappush(minheap, (int(mapped), i, num))
        
        ans = []
        while minheap:
            ans.append(heapq.heappop(minheap)[2])
        return ans