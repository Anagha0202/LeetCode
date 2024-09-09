class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        text1 = abcd    text2 = abd
        d==d => abc, ab  removing both characters because they would be a part of the subsequence and longest depends on the value of the remainign string

        text1 = abcd    text2 = abc
        d!=c => abcd, ab    and     abc, abc removing one character from each string to find the longest subsequence of either of them
        """
        # Bottom Up
        # t: O(n*m)
        # s: O(n*m)
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                row, col = i+1, j+1
                # print(text1[i], text2[j])
                if text1[i]==text2[j]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:            
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
                # print(dp)
        return dp[-1][-1]