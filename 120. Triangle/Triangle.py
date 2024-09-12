class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        adj[i] = nums[i+1][j], nums[i+1][j+1]
        
        Approach 1: DFS with memoization - Top Down
        start from i=0, traverse downwards until the end 
        from i=0, we can go down [i+1][j] or [i+1][j+1]
        when we reach the end of a branch, check if minimum and backtrack one node and go down [i+1][j+1]
        track the minimum value possible at each position in dictionary
        t: O(n^2)
        s: O(n^2)

        Approach 2: Bottom up
        Traverse from last level upwards.
        minimum you can get at each [i][j], store in min_path
        move upwards to row i-1
        minimum you can get from [i][j] + min([i+1][j],[i+1][j+1]), store in min_path
        t: O(n^2)
        s: O(n^2)
        """
        # Approach 1: Top DOwn
        rows = len(triangle)
        min_path = collections.defaultdict(int)
        visited = set()
        def backtrack(row, col):
            # Failure case
            if (row>=rows or col>=len(triangle[row])):
                    return 0
            # Sucess case
            if (row,col) in min_path:
                return min_path[(row,col)]
            
            left = backtrack(row+1, col)
            right = backtrack(row+1, col+1)
            min_path[(row,col)] = triangle[row][col] + min(left,right)
            return min_path[(row,col)]
        
        return backtrack(0,0)

        # Approach 2: Bottom up
        min_path = [[0]*len(triangle) for row in range(len(triangle))]
        min_path[len(triangle)-1] = triangle[len(triangle)-1]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                left = triangle[row][col] + min_path[row+1][col]
                right = triangle[row][col] + min_path[row+1][col+1]
                min_path[row][col] = min(left, right)
        
        return min_path[0][0]