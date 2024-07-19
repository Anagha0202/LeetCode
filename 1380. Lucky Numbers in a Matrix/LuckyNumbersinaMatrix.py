class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # Time: O(m*n)
        # Space: O(m*n)
        # Approach 2: 
        minrow = [min(r) for r in matrix]
        maxcol = [max(c) for c in zip(*matrix)] 
        return list(set(minrow) & set(maxcol))

        # Approach 1:
        mins, maxs = [math.inf]*len(matrix), [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                mins[i] = min(mins[i], matrix[i][j])
                maxs[j] = max(maxs[j], matrix[i][j])
        
        return list(set(mins) & set(maxs))