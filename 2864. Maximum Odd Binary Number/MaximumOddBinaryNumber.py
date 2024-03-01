class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = s.count('1')
        ans = []
        if count==0:
            return ''.join(ans)
        ans.append('1'*(count-1))
        ans.append('0'*(len(s)-count))
        ans.append('1')
        return ''.join(ans)
        # ans[-1] = '1'
        # count -= 1
        # i = 0
        # while count>0:
        #     ans[i] = '1'
        #     i+=1
        #     count -= 1
        # return ''.join(ans)