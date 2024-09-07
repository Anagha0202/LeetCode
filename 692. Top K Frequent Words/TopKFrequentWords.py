class pair:
    def __init__(self,word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, next_pair):
        if self.count==next_pair.count: # when counts are same, 
            return self.word>next_pair.word # higher is the one that comes first lexicographically so we add to the end of the heap
        else:
            return self.count<next_pair.count   

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Approach 1:
        track the count of each word in a hashmap 
        convert into list (count, word) of size k
        sort will sort based on the lowest frequency 
        if count is same, will sort based on the word which makes it lexicographical order
        if size of minheap>k, pop least count element and replace with new count element
        t: O(n+ nlogk)
        s: O(n + k)
        """
        minheap = []
        counts = collections.Counter(words)

        for word, count in counts.items():
            heapq.heappush(minheap, pair(word,count))
            while len(minheap)>k:
                heapq.heappop(minheap)

        return [word_pair.word for word_pair in sorted(minheap, reverse=True)]


        minheap = [] 
        counts = collections.Counter(words)

        for word, count in counts.items():
            minheap.append((count, word))
            minheap.sort(key=lambda w:(-w[0],w[1]))        
            # print(minheap)
            while len(minheap)>k:
                minheap.pop()
            # print(minheap)

        return [word for count, word in minheap]