class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Approach 1: BFS
        # Time: O(n*m)
        # space: O(n*m)

        rows, cols = len(mat), len(mat[0])
        q = deque([])
        dirs = [(0,-1), (-1,0), (0,1), (1,0)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1 # Setting as not seen
        
        while q:
            i, j = q.popleft()
            for r,c in dirs:
                if (i+r)<0 or (i+r)>=rows or (j+c)<0 or (j+c)>=cols or mat[i+r][j+c]!=-1: # checking if its a part of not seen 
                    continue
                mat[i+r][j+c] = mat[i][j] + 1
                q.append((i+r,j+c))
        return mat