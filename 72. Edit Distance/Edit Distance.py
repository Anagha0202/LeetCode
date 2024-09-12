class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Bottom up
        cache = [[math.inf]*(len(word2)+1) for _ in range(len(word1)+1)]
        
        for row in range(len(word1)+1):
            cache[row][len(word2)] = len(word1) - row
        for col in range(len(word2)+1):
            cache[len(word1)][col] = len(word2) - col
                
        for row in range(len(word1)-1, -1, -1):
            for col in range(len(word2)-1, -1, -1):
                if word1[row]==word2[col]:
                    cache[row][col] = cache[row+1][col+1]
                else:
                    cache[row][col] = 1 + min(cache[row+1][col+1], cache[row+1][col], cache[row][col+1])
        print(cache)
        return cache[0][0]

        # Top Down
        dp = collections.defaultdict(int)
        def dfs(i,j):
            if i>=len(word1) and j>=len(word2):
                return 0
            if i>=len(word1):
                return len(word2)-j
            if j>=len(word2):
                return len(word1)-i
            if (i,j) in dp:
                return dp[(i,j)]

            if word1[i]==word2[j]:
                return 0 + dfs(i+1, j+1)
            else:
                remove = 1 + dfs(i+1, j)
                add = 1 + dfs(i, j+1)
                replace = 1 + dfs(i+1, j+1)

                dp[(i,j)] = min(remove,add,replace)
                return dp[(i,j)]
        
        return dfs(0,0)