class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # turns = { -2:-1, -1:+1} 

        # 0      1     2      3   => (index+turns[])%4 
        # North, East, South, West
        # (0,1)  (1,0) (0,-1) (-1,0)
        # i      newi         newi

        def walk(x, y, dir, units, obstacles):
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            while units>0:
                new_x, new_y = x+directions[dir][0], y+directions[dir][1]
                if (new_x, new_y) in obstacles:
                    return (x,y)
                x= new_x
                y= new_y
                units-=1
            return (x,y)
        
        obstacles = set(map(tuple, obstacles))
        cur_x, cur_y = 0, 0
        turns = {-2:-1, -1:1}
        cur_dir = 0
        max_dist = 0

        for command in commands:
            if command in turns:
                cur_dir = (cur_dir+turns[command])%4
                continue
            cur_x, cur_y = walk(cur_x, cur_y, cur_dir, command, obstacles)
            max_dist = max(max_dist, (cur_x**2 + cur_y**2))
        return max_dist

