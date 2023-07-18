import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapify(max_heap)
        
        while len(max_heap)>1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)
            if x != y:
                y = -(abs(y) - abs(x))
                heapq.heappush(max_heap, y)
        return -(heapq.heappop(max_heap)) if max_heap else 0