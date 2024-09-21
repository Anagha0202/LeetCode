class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        # corner cases
        if rows==1 and cols==1:
            return 0
        
        # Manhattan distance is (x2-x1)+(y2-y1) is shortest grid path
        # so if number of available k > shortest grid path, then all blocks till end can be removed and manhattan distance will be shortest path to the end
        if k >= (rows+cols-2):
            return rows+cols-2
        
        # BFS
        queue = collections.deque([(0,0,k)]) # (row,col,k)
        visited = set()
        visited.add((0,0,k))
        directions = [(0,-1),(-1,0),(0,1),(1,0)]
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col, k = queue.popleft()
                if row==rows-1 and col==cols-1:
                    return steps
            
                for i in range(len(directions)):
                    new_row, new_col = row+directions[i][0], col+directions[i][1]
                    if new_row<0 or new_row==rows or new_col<0 or new_col==cols:
                        continue
                    new_k = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_k)
                    if new_k>=0 and new_state not in visited:
                        queue.append(new_state)
                        visited.add(new_state)
            steps+=1
        
        return -1