class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        n = len(s)
        ans = []
        curlen = len(str(low))
        maxlen = len(str(high))

        while curlen<=maxlen:
            i = 0
            while i<(n-curlen+1):
                temp = int(s[i:i+curlen])
                if low<=temp<=high:
                    ans.append(temp)
                i+=1
            curlen+=1
        
        return ans