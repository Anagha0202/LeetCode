class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #slope = (y2-y1)/(x2-x1)
        #find slope as a pair for all pairs of points passing through one point
        #maintain hashmap with slope as key and count the points that pass through given slope for each point
        #need to bring the slope values to similar values so that although slope values maybe different, but they lie on the same slope. 
        #reduce each slope by gcd to get to the lowest number possible so that all similar slopes will get grouped into same key
        #t: O(n^2logn) s: O(n)
        def generate_gcd(x, y):
            return x if y==0 else generate_gcd(y, x%y)
        
        max_points = 0
        slopes = collections.defaultdict(int)
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            overlap = 1 #starts with 1 for point (x1,y1) overlaps with itself and needs to be considered as 1 point on the line
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                slope_y = (y2-y1)
                slope_x = (x2-x1)
                if slope_y==0 and slope_x==0: 
                    # (x2,y2) has same co-ordinates as (x1,y1) so overlaps 
                    overlap+=1
                    continue
                # convert each pair down to its lowest possible values so that all similar pairs can be brought down to same value to group
                gcd = generate_gcd(slope_y, slope_x)
                if gcd!=0:
                    slope_x = slope_x//gcd
                    slope_y = slope_y//gcd

                slopes[(slope_x, slope_y)]+=1

            mx = max(list(slopes.values())) if slopes else 0 #in case of last point, slopes will not have any values

            max_points = max(max_points, mx+overlap)
            slopes.clear() #clear the slopes to calculates slopes through different (x1,y1)
        return max_points