class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # Time : O(1)
        # Space : O(1)

        # Base: Finding x distance and y distance
        diff_sxfx = abs(sx-fx)
        # print("diff_sxfx=", diff_sxfx)
        diff_syfy = abs(sy-fy)
        # print("diff_syfy=", diff_syfy)
        
        # Condition 1: When start and finish are in the same box
        # in this case if t = 1, then in one move we can move to any other box but cannot come back to the finish box. Hence False
        # But, in this case if t >= 2, then we can move back and forth around the finish box each time and ensure to reach the finish (start) box in t time

        if diff_sxfx==0 and diff_syfy==0:
            if t==1:
                return False
            else:
                return True

        # Condition 2: When x dist<=t and y dist<=t then reachable
        # In the worst condition where we have to move diagonally to reach the finish box, we will increase both at the same time => the distance of both should be less than or exactly equal to the time

        if diff_sxfx<=t and diff_syfy<=t:
            return True
        else:
            return False

############################################################################################################################################















        dp = collections.defaultdict(bool)
        def helper(cx, cy, timer):
            print("current (cx,cy)=", cx,cy)
            print("current timer=", timer)
            if (cx,cy,timer) in dp:
                print("in dp")
                return dp[(cx,cy)]
            if timer==t :
                if cx==fx and cy==fy:
                    print("Found destination")
                    dp[(cx,cy,timer)] = True
                    return True
                else:
                    print("Timed out")
                    dp[(cx,cy,timer)] = False
                    return False
            # else:
            #     if (cx not in range(sx,fx+1) or 
            #         cy not in range(sy,fy+1)):
            #         dp[(cx,cy,timer)] = False
            #         return False
                
                
            
            dirs = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
            for dx, dy in dirs:
                if helper(cx+dx, cy+dy, timer+1):
                    return True
            return False
        
        return helper(sx, sy, 0)
                
        