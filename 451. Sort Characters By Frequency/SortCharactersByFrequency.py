class Solution:
    def frequencySort(self, s: str) -> str:
        # Approach 2: Using max heap instead of sort
        res = []
        count = dict(collections.Counter(s))
        maxheap = []
        for ch, val in count.items():
            heapq.heappush(maxheap, (-val, ch))
        while maxheap:
            val, ch = heapq.heappop(maxheap)
            res.append(ch*abs(val))
        return ''.join(res)
        
        # Approach 1: Using sorted Dict of counts
        count = dict(collections.Counter(s))
        count = dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
        # print(count)
        return ''.join([ch*val for ch, val in count.items()])