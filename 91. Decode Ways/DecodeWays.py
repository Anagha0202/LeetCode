class Solution:
    def numDecodings(self, s: str) -> int:
        # Bottom - Up
        ways = [0]*(len(s)+1)
        ways[-1] = 1

        for index in range(len(s)-1, -1, -1):
            if s[index]!='0':
                ways[index] = ways[index+1]
            if (index+1 in range(len(s))) and ((s[index]=='1') or (s[index]=='2' and s[index+1]<='6')):
                ways[index] += ways[index+2]
        
        return ways[0]

        # Top - Down
        # dfs down till single digit which has only one way to split
        # if a digit is non-zero, can it can be split inidvidually recursively
        # consider current digit and next digit to form 2 digit number and if the number is between 1 and 26 then split the rest of the string considering these 2 together
        # t: O(n)
        # s: O(n)
        @lru_cache(None)
        def decode(index):
            if index==len(s):
                return 1 #last digit can  be split individually
            ans = 0
            if s[index]!='0':
                ans+= decode(index+1) #take single digits

            if (index+1 < len(s)) and ((s[index]=='1') or (s[index]=='2' and s[index+1]<='6')):
                # consider 2 digits together, if together valid then check split of grouping together
                ans+= decode(index+2)
            return ans
        
        return decode(0)