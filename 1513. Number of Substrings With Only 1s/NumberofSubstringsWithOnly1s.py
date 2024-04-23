class Solution:
    def numSub(self, s: str) -> int:
        count, total = 0, 0
        for n in s:
            if n=='0':
                count = 0
            else : 
                count+=1
                total+=count
        return (total%(pow(10,9)+7))