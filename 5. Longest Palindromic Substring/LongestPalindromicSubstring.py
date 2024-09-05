class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[None]*len(s) for _ in range(len(s))]
        max_len = 0
        longest_p = ""

        for i in range(n):
            dp[i][i] = True
        max_len = 1
        longest_p = s[0]
        
        for substring_len in range(1,n):
            start = 0
            while start+substring_len<n:
                end = start+substring_len
                if s[start]==s[end] and (dp[start+1][end-1]==True or dp[start+1][end-1]==None):
                    dp[start][end] = True
                    if len(s[start:end+1])>max_len:
                        max_len = len(s[start:end+1])
                        longest_p = s[start:end+1]
                else:
                    dp[start][end] = False
                start+=1
        
        return longest_p

