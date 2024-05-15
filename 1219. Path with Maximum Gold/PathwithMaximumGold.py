class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def helper(seen, r, c):
            # print("r={} c={} seen={}".format(r, c, seen))
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0 or 
                (r,c) in seen):
                # print("breaking condition")
                return 0
            seen.add((r,c))
            # print("new seen={}".format(seen))
            
            collect= grid[r][c] + max(helper(seen, r-1, c), 
                                        helper(seen, r, c-1),
                                        helper(seen, r+1, c),
                                        helper(seen, r, c+1))
            # print("new collect={}.\nEND".format(collect))
            seen.discard((r,c))
            return collect
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                # print("initial r={} c={}".format(r, c))
                res = max(res, helper(set(), r, c))
                # print("current res=", res)
        
        return res