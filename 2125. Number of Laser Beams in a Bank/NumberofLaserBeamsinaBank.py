class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Approach 2:
        lasers, cur_sec, prev_sec = 0, 0, 0

        for i in bank:
            cur_sec = i.count('1')
            if cur_sec==0:
                continue
            lasers += (cur_sec*prev_sec)
            prev_sec = cur_sec 
            # print("lasers={} cur_sec={} prev_sec={}".format(lasers, cur_sec, prev_sec))
        
        return lasers

        # Approach 1:

        lasers = 0
        counts = collections.defaultdict(lambda: 0)

        for i in range(len(bank)):
            for j in range(len(bank[0])):
                counts[i]+= int(bank[i][j])

        for i in range(1, len(counts)):
            if counts[i-1]>0:
                lasers += (counts[i]*counts[i-1])
                continue
            itr = 2
            while i-itr in range(len(counts)) and counts[i-itr]==0:
                itr+=1
            lasers += (counts[i]*counts[i-itr])
        
        return lasers