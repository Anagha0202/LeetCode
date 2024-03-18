class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[1])
        arrow = points[0][1]
        count = 1
        for (x1, x2) in points[1:]:
            if x1<=arrow<=x2:
                continue
            else:
                count+=1
                arrow=x2
        return count            